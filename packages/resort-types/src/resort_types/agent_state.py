import operator
from typing import Annotated, TypedDict

from langgraph.graph.message import add_messages


class ResortAgentState(TypedDict):
    messages: Annotated[list, add_messages]

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
