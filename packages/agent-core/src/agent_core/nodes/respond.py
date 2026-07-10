from __future__ import annotations

import json
from datetime import date

from langchain_core.messages import AIMessage, SystemMessage

from agent_core.config import get_llm
from agent_core.prompts.system import build_system_prompt


def call_agent(state: dict, store: Any = None) -> dict:
    """Call the LLM with tools to process the request."""
    llm = get_llm()
    system_prompt = build_system_prompt()

    messages = [SystemMessage(content=system_prompt)] + list(state.get("messages", []))

    bound_llm = llm.bind_tools([])

    response = bound_llm.invoke(messages)

    return {
        "messages": [response],
        "current_step": "agent_responded",
        "step_count": state.get("step_count", 0) + 1,
    }


def respond_to_guest(state: dict) -> dict:
    """Generate a draft guest reply based on gathered context."""
    llm = get_llm()
    system_prompt = build_system_prompt()

    messages = [SystemMessage(content=system_prompt)] + list(state.get("messages", []))

    response = llm.invoke(messages)

    return {
        "messages": [AIMessage(content=response.content)],
        "current_step": "responded",
        "step_count": state.get("step_count", 0) + 1,
    }
