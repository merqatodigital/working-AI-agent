from __future__ import annotations

import operator
from typing import Annotated, Any, Literal, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    intent: str
    urgency: str
    department: str
    guest_id: str | None
    reservation_id: str | None
    room_id: str | None
    proposed_action: dict | None
    approval_required: bool
    approval_type: str | None
    audit_entries: Annotated[list[dict], operator.add]
    brief_update: str | None
    current_step: str
    step_count: int
    max_steps: int


def build_graph(
    store: Any = None,
    tools: list | None = None,
    checkpointer: Any = None,
):
    """Build the KAPWA resort agent graph."""
    from resort_tools import ALL_TOOLS
    from agent_core.nodes.classify import classify_intent
    from agent_core.nodes.audit import log_audit

    if tools is None:
        tools = ALL_TOOLS

    def classify_node(state: AgentState) -> dict:
        return classify_intent(state)

    def agent_node(state: AgentState) -> dict:
        from agent_core.config import get_llm
        from agent_core.prompts.system import build_system_prompt
        from langchain_core.messages import SystemMessage

        llm = get_llm()
        system_prompt = build_system_prompt()
        messages = [SystemMessage(content=system_prompt)] + list(state.get("messages", []))

        bound_llm = llm.bind_tools(tools)
        response = bound_llm.invoke(messages)

        return {
            "messages": [response],
            "current_step": "agent_responded",
            "step_count": state.get("step_count", 0) + 1,
        }

    def audit_node(state: AgentState) -> dict:
        return log_audit(state, store)

    builder = StateGraph(AgentState)

    builder.add_node("classify", classify_node)
    builder.add_node("agent", agent_node)
    builder.add_node("tools", ToolNode(tools))
    builder.add_node("audit", audit_node)

    builder.add_edge(START, "classify")
    builder.add_edge("classify", "agent")
    builder.add_conditional_edges("agent", tools_condition, {
        "tools": "tools",
        END: "audit",
    })
    builder.add_edge("tools", "agent")
    builder.add_edge("audit", END)

    return builder.compile(checkpointer=checkpointer)
