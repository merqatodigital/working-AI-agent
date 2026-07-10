from __future__ import annotations

from typing import TYPE_CHECKING

from langchain_core.tools import tool

if TYPE_CHECKING:
    from resort_data.loader import ResortDataStore

_store: ResortDataStore | None = None


def set_store(store: ResortDataStore) -> None:
    global _store
    _store = store


def _get_store() -> ResortDataStore:
    if _store is None:
        raise RuntimeError("ResortDataStore not initialized. Call set_store() first.")
    return _store


@tool
def get_reservation(reservation_id: str) -> str:
    """Look up a reservation by ID. Returns guest name, dates, room, status, and balance."""
    store = _get_store()
    r = store.get_reservation(reservation_id)
    if not r:
        return f"Reservation {reservation_id} not found."
    guest = store.get_guest(r["guest_id"])
    room = store.get_room(r["room_id"]) if r.get("room_id") else None
    guest_name = f"{guest['first_name']} {guest['last_name']}" if guest else "Unknown"
    room_num = room["room_number"] if room else "N/A"
    balance = r["total_amount"] - r["paid_amount"]
    return (
        f"Reservation {r['id']}: {guest_name} | Room {room_num} ({r['room_type']}) | "
        f"{r['check_in_date']} to {r['check_out_date']} | Status: {r['status']} | "
        f"Total: PHP {r['total_amount']:,.0f} | Paid: PHP {r['paid_amount']:,.0f} | Balance: PHP {balance:,.0f}"
    )


@tool
def check_room_availability(check_in: str, check_out: str, room_type: str = "any") -> str:
    """Check which rooms are available for given dates and optional room type."""
    store = _get_store()
    rooms = store.get_available_rooms(room_type=room_type if room_type != "any" else None)
    if not rooms:
        return f"No rooms available for {check_in} to {check_out}."
    lines = [f"Available rooms ({check_in} to {check_out}):"]
    for r in rooms:
        lines.append(f"  {r['room_number']} | {r['room_type']} | Floor {r['floor']} | PHP {r['base_rate']:,.0f}/night")
    return "\n".join(lines)


@tool
def get_guest_profile(guest_id: str) -> str:
    """Get guest profile including name, preferences, past stays, and notes."""
    store = _get_store()
    g = store.get_guest(guest_id)
    if not g:
        return f"Guest {guest_id} not found."
    prefs = ", ".join(f"{k}={v}" for k, v in g.get("preferences", {}).items()) if g.get("preferences") else "None"
    past = len(g.get("past_stays", []))
    return (
        f"Guest {g['id']}: {g['first_name']} {g['last_name']} | {g.get('nationality', 'N/A')} | "
        f"Email: {g.get('email', 'N/A')} | Phone: {g.get('phone', 'N/A')} | "
        f"Loyalty: {g.get('loyalty_tier', 'standard')} | Past stays: {past} | "
        f"Preferences: {prefs} | Notes: {g.get('notes', 'None')}"
    )


@tool
def get_staff_on_shift(department: str = "all") -> str:
    """Get current staff on shift, optionally filtered by department."""
    store = _get_store()
    staff = store.get_staff_on_shift(department=department if department != "all" else None)
    if not staff:
        return f"No staff on shift in {department}."
    lines = [f"Staff on shift ({department}):"]
    for s in staff:
        lines.append(f"  {s['first_name']} {s['last_name']} | {s['role']} | {s['department']} | ID: {s['id']}")
    return "\n".join(lines)


@tool
def get_stock_level(category: str = "all") -> str:
    """Get current inventory levels, optionally filtered by category."""
    store = _get_store()
    items = store.get_stock_level(category=category if category != "all" else None)
    if not items:
        return f"No inventory items found."
    low = [i for i in items if i["current_quantity"] <= i["min_quantity"]]
    lines = [f"Inventory ({len(items)} items" + (f", {len(low)} LOW)" if low else ")")]
    for i in items:
        flag = " ⚠️ LOW" if i["current_quantity"] <= i["min_quantity"] else ""
        lines.append(
            f"  {i['item_name']} | {i['category']} | Qty: {i['current_quantity']} {i['unit']} "
            f"(min: {i['min_quantity']}) | Unit cost: PHP {i['unit_cost']:,.0f} | Supplier: {i.get('supplier', 'N/A')}{flag}"
        )
    return "\n".join(lines)


@tool
def get_room_status(room_id: str = "all") -> str:
    """Get room status. Pass a room ID for a specific room, or 'all' for summary."""
    store = _get_store()
    if room_id == "all":
        rooms = list(store.rooms.values())
        status_counts = {}
        for r in rooms:
            status_counts[r["status"]] = status_counts.get(r["status"], 0) + 1
        lines = [f"Room status summary ({len(rooms)} total):"]
        for status, count in sorted(status_counts.items()):
            lines.append(f"  {status}: {count}")
        return "\n".join(lines)
    room = store.get_room(room_id)
    if not room:
        return f"Room {room_id} not found."
    return (
        f"Room {room['room_number']}: {room['room_type']} | Floor {room['floor']} | "
        f"Status: {room['status']} | Rate: PHP {room['base_rate']:,.0f}/night | "
        f"Last cleaned: {room.get('last_cleaned_at', 'N/A')} | "
        f"Notes: {room.get('maintenance_notes', 'None')}"
    )
