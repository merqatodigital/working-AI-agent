from __future__ import annotations

from typing import Any


def log_audit(state: dict, store: Any = None) -> dict:
    """Log the current action to the audit trail."""
    intent = state.get("intent", "general")
    department = state.get("department", "front_desk")
    step = state.get("current_step", "unknown")

    if store:
        store.add_audit_entry(
            action=f"agent_{intent}",
            department=department,
            agent_step=step,
            guest_id=state.get("guest_id"),
            reservation_id=state.get("reservation_id"),
            details={
                "urgency": state.get("urgency", "normal"),
                "step_count": state.get("step_count", 0),
            },
        )

    return {
        "current_step": "audit_logged",
        "step_count": state.get("step_count", 0) + 1,
    }
