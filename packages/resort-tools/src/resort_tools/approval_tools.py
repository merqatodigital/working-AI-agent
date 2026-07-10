from __future__ import annotations

from langchain_core.tools import tool

from .reservation_tools import _get_store

SENSITIVE_TOOLS = {"refund_guest", "create_purchase_request", "change_room_price"}


@tool
def refund_guest(guest_id: str, amount: float, reason: str) -> str:
    """Propose a guest refund. REQUIRES MANAGER APPROVAL before execution. Use for complaints, overcharges, or goodwill gestures."""
    store = _get_store()
    guest = store.get_guest(guest_id)
    if not guest:
        return f"Guest {guest_id} not found."
    guest_name = f"{guest['first_name']} {guest['last_name']}"
    approval = store.request_approval(
        approval_type="refund",
        action_type="guest_refund",
        payload={"guest_id": guest_id, "amount": amount, "reason": reason},
    )
    store.add_audit_entry(
        action="refund_proposed",
        department="finance",
        guest_id=guest_id,
        details={"amount": amount, "reason": reason, "approval_id": approval["id"]},
    )
    return (
        f"Refund of PHP {amount:,.0f} proposed for {guest_name}. "
        f"Reason: {reason}. "
        f"Approval ID: {approval['id']} — requires manager approval."
    )


@tool
def create_purchase_request(item: str, quantity: int, supplier: str, estimated_cost: float) -> str:
    """Propose a purchase request for inventory. REQUIRES MANAGER APPROVAL before ordering."""
    store = _get_store()
    approval = store.request_approval(
        approval_type="purchase_approval",
        action_type="purchase_request",
        payload={
            "item": item,
            "quantity": quantity,
            "supplier": supplier,
            "estimated_cost": estimated_cost,
        },
    )
    store.add_audit_entry(
        action="purchase_proposed",
        department="inventory",
        details={
            "item": item,
            "quantity": quantity,
            "supplier": supplier,
            "estimated_cost": estimated_cost,
            "approval_id": approval["id"],
        },
    )
    return (
        f"Purchase request: {quantity} x {item} from {supplier} | Est. cost: PHP {estimated_cost:,.0f}. "
        f"Approval ID: {approval['id']} — requires manager approval."
    )


@tool
def change_room_price(room_id: str, new_rate: float) -> str:
    """Change room rate. REQUIRES MANAGER APPROVAL before applying."""
    store = _get_store()
    room = store.get_room(room_id)
    if not room:
        return f"Room {room_id} not found."
    old_rate = room["base_rate"]
    approval = store.request_approval(
        approval_type="price_change",
        action_type="room_rate_change",
        payload={"room_id": room_id, "old_rate": old_rate, "new_rate": new_rate},
    )
    store.add_audit_entry(
        action="price_change_proposed",
        department="reservations",
        details={
            "room_number": room["room_number"],
            "old_rate": old_rate,
            "new_rate": new_rate,
            "approval_id": approval["id"],
        },
    )
    return (
        f"Rate change proposed for room {room['room_number']}: PHP {old_rate:,.0f} → PHP {new_rate:,.0f}. "
        f"Approval ID: {approval['id']} — requires manager approval."
    )
