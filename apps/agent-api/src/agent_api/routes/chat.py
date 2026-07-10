from __future__ import annotations

import json
import traceback
from typing import AsyncGenerator

from fastapi import APIRouter
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse

from agent_api.deps import get_agent, get_store

router = APIRouter(tags=["chat"])


class ChatRequest(BaseModel):
    message: str
    thread_id: str = "default"


class ChatResponse(BaseModel):
    response: str
    intent: str = ""
    department: str = ""
    urgency: str = ""
    step_count: int = 0


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        from langchain_core.messages import HumanMessage

        agent = get_agent()
        store = get_store()

        initial_state = {
            "messages": [HumanMessage(content=req.message)],
            "intent": "",
            "urgency": "",
            "department": "",
            "guest_id": None,
            "reservation_id": None,
            "room_id": None,
            "proposed_action": None,
            "approval_required": False,
            "approval_type": None,
            "audit_entries": [],
            "brief_update": None,
            "current_step": "",
            "step_count": 0,
            "max_steps": 10,
        }

        config = {"configurable": {"thread_id": req.thread_id}}
        result = agent.invoke(initial_state, config=config)

        messages = result.get("messages", [])
        content = ""
        if messages:
            last = messages[-1]
            content = last.content if hasattr(last, "content") else str(last)

        return ChatResponse(
            response=content,
            intent=result.get("intent") or "",
            department=result.get("department") or "",
            urgency=result.get("urgency") or "",
            step_count=result.get("step_count") or 0,
        )
    except Exception as e:
        traceback.print_exc()
        raise


@router.get("/chat/stream")
async def chat_stream(message: str, thread_id: str = "default"):
    from langchain_core.messages import HumanMessage

    agent = get_agent()

    initial_state = {
        "messages": [HumanMessage(content=message)],
        "intent": "",
        "urgency": "",
        "department": "",
        "guest_id": None,
        "reservation_id": None,
        "room_id": None,
        "proposed_action": None,
        "approval_required": False,
        "approval_type": None,
        "audit_entries": [],
        "brief_update": None,
        "current_step": "",
        "step_count": 0,
        "max_steps": 10,
    }

    config = {"configurable": {"thread_id": thread_id}}

    async def event_generator() -> AsyncGenerator[dict, None]:
        try:
            async for event in agent.astream(initial_state, config=config, stream_mode="updates"):
                for node_name, node_output in event.items():
                    if node_name == "agent" and "messages" in node_output:
                        for msg in node_output["messages"]:
                            if hasattr(msg, "content") and msg.content:
                                yield {
                                    "event": "message",
                                    "data": json.dumps({
                                        "type": "agent",
                                        "content": msg.content,
                                    }),
                                }
                    elif node_name == "classify":
                        yield {
                            "event": "classify",
                            "data": json.dumps({
                                "intent": node_output.get("intent", ""),
                                "department": node_output.get("department", ""),
                                "urgency": node_output.get("urgency", ""),
                            }),
                        }
                    elif node_name == "audit":
                        yield {
                            "event": "audit",
                            "data": json.dumps({
                                "action": "audit_logged",
                                "step": node_output.get("current_step", ""),
                            }),
                        }
            yield {"event": "done", "data": "{}"}
        except Exception as e:
            yield {"event": "error", "data": json.dumps({"error": str(e)})}

    return EventSourceResponse(event_generator())
