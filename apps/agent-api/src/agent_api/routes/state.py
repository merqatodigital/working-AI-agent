from __future__ import annotations

from fastapi import APIRouter

from agent_api.deps import get_store

router = APIRouter(tags=["state"])


@router.get("/state")
def get_resort_state():
    store = get_store()
    rooms = list(store.rooms.values())
    active_res = [r for r in store.reservations.values() if r["status"] == "checked_in"]
    open_tasks = [t for t in store.tasks.values() if t["status"] not in ("completed", "cancelled")]
    low_stock = store.get_low_stock_items()
    pending = store.get_pending_approvals()

    status_counts = {}
    for r in rooms:
        status_counts[r["status"]] = status_counts.get(r["status"], 0) + 1

    total_rooms = len(rooms)
    occupied = status_counts.get("occupied", 0)
    occupancy = (occupied / total_rooms * 100) if total_rooms > 0 else 0

    return {
        "occupancy_rate": round(occupancy, 1),
        "total_rooms": total_rooms,
        "rooms_by_status": status_counts,
        "guests_checked_in": len(active_res),
        "active_reservations": len(active_res),
        "open_tasks": len(open_tasks),
        "low_stock_items": len(low_stock),
        "pending_approvals": len(pending),
        "audit_entries_today": len(store.audit_log),
    }


@router.get("/guests")
def list_guests():
    store = get_store()
    return {"guests": list(store.guests.values())}


@router.get("/guests/{guest_id}")
def get_guest(guest_id: str):
    store = get_store()
    guest = store.get_guest(guest_id)
    if not guest:
        return {"error": f"Guest {guest_id} not found"}
    return {"guest": guest}


@router.get("/rooms")
def list_rooms():
    store = get_store()
    return {"rooms": list(store.rooms.values())}


@router.get("/tasks")
def list_tasks(department: str | None = None):
    store = get_store()
    tasks = store.get_open_tasks(department=department)
    return {"tasks": tasks}


@router.get("/staff")
def list_staff(department: str | None = None):
    store = get_store()
    staff = store.get_staff_on_shift(department=department)
    return {"staff": staff}
