from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

from agent_api.deps import get_store

router = APIRouter(tags=["approvals"])


class ApprovalDecision(BaseModel):
    approved: bool
    notes: str = ""


@router.get("/approvals/pending")
def get_pending_approvals():
    store = get_store()
    return {"approvals": store.get_pending_approvals()}


@router.post("/approvals/{approval_id}/decide")
def decide_approval(approval_id: str, decision: ApprovalDecision):
    store = get_store()
    result = store.resolve_approval(approval_id, decision.approved, decision.notes)
    if not result:
        return {"error": f"Approval {approval_id} not found"}
    store.add_audit_entry(
        action="approval_resolved",
        details={
            "approval_id": approval_id,
            "approved": decision.approved,
            "notes": decision.notes,
        },
    )
    return {"approval": result}
