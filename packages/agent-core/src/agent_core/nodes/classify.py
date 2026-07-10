from __future__ import annotations

import json
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage

from agent_core.config import get_llm
from agent_core.prompts.classify import INTENT_CLASSIFICATION_PROMPT


def classify_intent(state: dict) -> dict:
    """Classify user intent into department and urgency."""
    llm = get_llm()
    messages = state.get("messages", [])
    if not messages:
        return {
            "intent": "general",
            "urgency": "normal",
            "department": "front_desk",
            "current_step": "classified",
        }

    last_msg = messages[-1]
    content = last_msg.content if hasattr(last_msg, "content") else str(last_msg)

    response = llm.invoke([
        SystemMessage(content=INTENT_CLASSIFICATION_PROMPT),
        HumanMessage(content=content),
    ])

    try:
        parsed = json.loads(response.content)
    except json.JSONDecodeError:
        parsed = {
            "intent": "general",
            "urgency": "normal",
            "department": "front_desk",
        }

    return {
        "intent": parsed.get("intent", "general"),
        "urgency": parsed.get("urgency", "normal"),
        "department": parsed.get("department", "front_desk"),
        "guest_id": parsed.get("guest_id"),
        "room_id": parsed.get("room_id"),
        "reservation_id": parsed.get("reservation_id"),
        "current_step": "classified",
        "step_count": state.get("step_count", 0) + 1,
    }
