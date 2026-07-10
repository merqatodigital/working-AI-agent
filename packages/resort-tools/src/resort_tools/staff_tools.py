from __future__ import annotations

from langchain_core.tools import tool

from .reservation_tools import _get_store


@tool
def create_task(
    department: str,
    title: str,
    description: str = "",
    priority: str = "normal",
    room_id: str | None = None,
    guest_id: str | None = None,
    reservation_id: str | None = None,
) -> str:
    """Create a resort task and assign to a department. Use for maintenance, housekeeping, guest relations, etc."""
    store = _get_store()
    task = store.create_task(
        department=department,
        title=title,
        description=description,
        priority=priority,
        room_id=room_id,
        guest_id=guest_id,
        reservation_id=reservation_id,
    )
    return f"Task created: {task['id']} | {task['title']} | Dept: {task['department']} | Priority: {task['priority']} | Status: {task['status']}"


@tool
def assign_task(task_id: str, staff_id: str) -> str:
    """Assign a task to a specific staff member."""
    store = _get_store()
    result = store.assign_task(task_id, staff_id)
    if not result:
        return f"Failed to assign task {task_id} to staff {staff_id}. Check IDs exist."
    staff = store.get_staff_member(staff_id)
    staff_name = f"{staff['first_name']} {staff['last_name']}" if staff else staff_id
    return f"Task {task_id} assigned to {staff_name}. Status updated to assigned."


@tool
def draft_guest_reply(guest_id: str, message: str) -> str:
    """Draft a reply to a guest. Returns the draft for review before sending."""
    store = _get_store()
    guest = store.get_guest(guest_id)
    if not guest:
        return f"Guest {guest_id} not found."
    guest_name = f"{guest['first_name']} {guest['last_name']}"
    return f"Draft reply to {guest_name} ({guest_id}):\n\n{message}\n\n[Draft created — ready for manager review before sending]"


@tool
def update_room_status(room_id: str, status: str) -> str:
    """Update room cleaning/maintenance status. Valid statuses: available, occupied, cleaning, maintenance, out_of_order."""
    store = _get_store()
    result = store.update_room_status(room_id, status)
    if not result:
        return f"Room {room_id} not found."
    return f"Room {result['room_number']} status updated to: {status}"


@tool
def record_task_completion(task_id: str, notes: str = "") -> str:
    """Mark a task as completed with optional notes."""
    store = _get_store()
    result = store.complete_task(task_id, notes)
    if not result:
        return f"Task {task_id} not found."
    return f"Task {task_id} ({result['title']}) marked as completed. Notes: {notes or 'None'}"


@tool
def record_check_in(reservation_id: str) -> str:
    """Record guest check-in. Updates reservation status and room status."""
    store = _get_store()
    r = store.get_reservation(reservation_id)
    if not r:
        return f"Reservation {reservation_id} not found."
    r["status"] = "checked_in"
    if r.get("room_id"):
        room = store.get_room(r["room_id"])
        if room:
            room["status"] = "occupied"
            return (
                f"Check-in recorded for reservation {reservation_id}. "
                f"Room {room['room_number']} status updated to occupied."
            )
    return f"Check-in recorded for reservation {reservation_id}."
