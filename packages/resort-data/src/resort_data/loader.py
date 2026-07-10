from __future__ import annotations

import json
from pathlib import Path
from typing import Any

MOCK_DIR = Path(__file__).parent / "mock"


class ResortDataStore:
    """In-memory resort data store. Source of truth for MVP."""

    def __init__(self) -> None:
        self.guests: dict[str, dict] = {}
        self.reservations: dict[str, dict] = {}
        self.rooms: dict[str, dict] = {}
        self.staff: dict[str, dict] = {}
        self.inventory: dict[str, dict] = {}
        self.tasks: dict[str, dict] = {}
        self.audit_log: list[dict] = []
        self.pending_approvals: list[dict] = []
        self.policies: dict[str, Any] = {}
        self._task_counter: int = 0

    @classmethod
    def load_from_mock(cls) -> ResortDataStore:
        store = cls()
        store.guests = _load_json("guests.json", key="id")
        store.reservations = _load_json("reservations.json", key="id")
        store.rooms = _load_json("rooms.json", key="id")
        store.staff = _load_json("staff.json", key="id")
        store.inventory = _load_json("inventory.json", key="id")
        store.policies = _load_json_raw("policies.json")
        return store

    def get_guest(self, guest_id: str) -> dict | None:
        return self.guests.get(guest_id)

    def find_guest_by_name(self, name: str) -> dict | None:
        name_lower = name.lower()
        for g in self.guests.values():
            full = f"{g['first_name']} {g['last_name']}".lower()
            if name_lower in full:
                return g
        return None

    def get_reservation(self, reservation_id: str) -> dict | None:
        return self.reservations.get(reservation_id)

    def get_reservations_by_guest(self, guest_id: str) -> list[dict]:
        return [r for r in self.reservations.values() if r["guest_id"] == guest_id]

    def get_active_reservations(self) -> list[dict]:
        return [r for r in self.reservations.values() if r["status"] == "checked_in"]

    def get_room(self, room_id: str) -> dict | None:
        return self.rooms.get(room_id)

    def get_room_by_number(self, room_number: str) -> dict | None:
        for r in self.rooms.values():
            if r["room_number"] == room_number:
                return r
        return None

    def get_available_rooms(
        self, check_in: str | None = None, check_out: str | None = None, room_type: str | None = None
    ) -> list[dict]:
        rooms = [r for r in self.rooms.values() if r["status"] == "available"]
        if room_type:
            rooms = [r for r in rooms if r["room_type"] == room_type]
        return rooms

    def get_staff_on_shift(self, department: str | None = None) -> list[dict]:
        active = [s for s in self.staff.values() if s["is_active"]]
        if department:
            active = [s for s in active if s["department"] == department]
        return active

    def get_staff_member(self, staff_id: str) -> dict | None:
        return self.staff.get(staff_id)

    def get_stock_level(self, category: str | None = None) -> list[dict]:
        items = list(self.inventory.values())
        if category:
            items = [i for i in items if i["category"] == category]
        return items

    def get_low_stock_items(self) -> list[dict]:
        return [i for i in self.inventory.values() if i["current_quantity"] <= i["min_quantity"]]

    def create_task(
        self,
        department: str,
        title: str,
        description: str = "",
        priority: str = "normal",
        room_id: str | None = None,
        guest_id: str | None = None,
        reservation_id: str | None = None,
    ) -> dict:
        self._task_counter += 1
        task_id = f"TK-{self._task_counter:04d}"
        task = {
            "id": task_id,
            "department": department,
            "title": title,
            "description": description,
            "priority": priority,
            "status": "pending",
            "assigned_to": None,
            "room_id": room_id,
            "guest_id": guest_id,
            "reservation_id": reservation_id,
            "created_by": "agent",
        }
        self.tasks[task_id] = task
        return task

    def assign_task(self, task_id: str, staff_id: str) -> dict | None:
        task = self.tasks.get(task_id)
        staff = self.staff.get(staff_id)
        if task and staff:
            task["assigned_to"] = staff_id
            task["status"] = "assigned"
            return task
        return None

    def complete_task(self, task_id: str, notes: str = "") -> dict | None:
        task = self.tasks.get(task_id)
        if task:
            task["status"] = "completed"
            task["completion_notes"] = notes
            return task
        return None

    def get_open_tasks(self, department: str | None = None) -> list[dict]:
        tasks = [t for t in self.tasks.values() if t["status"] not in ("completed", "cancelled")]
        if department:
            tasks = [t for t in tasks if t["department"] == department]
        return tasks

    def add_audit_entry(self, action: str, **kwargs: Any) -> dict:
        entry = {"action": action, **kwargs}
        self.audit_log.append(entry)
        return entry

    def request_approval(
        self, approval_type: str, action_type: str, payload: dict, requested_by: str = "agent"
    ) -> dict:
        approval = {
            "id": f"APR-{len(self.pending_approvals) + 1:04d}",
            "approval_type": approval_type,
            "action_type": action_type,
            "payload": payload,
            "status": "pending",
            "requested_by": requested_by,
        }
        self.pending_approvals.append(approval)
        return approval

    def get_pending_approvals(self) -> list[dict]:
        return [a for a in self.pending_approvals if a["status"] == "pending"]

    def resolve_approval(self, approval_id: str, approved: bool, notes: str = "") -> dict | None:
        for a in self.pending_approvals:
            if a["id"] == approval_id:
                a["status"] = "approved" if approved else "rejected"
                a["notes"] = notes
                return a
        return None

    def get_policy(self, key: str) -> Any:
        return self.policies.get(key)

    def update_room_status(self, room_id: str, status: str) -> dict | None:
        room = self.rooms.get(room_id)
        if room:
            room["status"] = status
            return room
        return None


def _load_json(filename: str, key: str = "id") -> dict[str, dict]:
    path = MOCK_DIR / filename
    with open(path) as f:
        data = json.load(f)
    return {item[key]: item for item in data}


def _load_json_raw(filename: str) -> dict:
    path = MOCK_DIR / filename
    with open(path) as f:
        return json.load(f)
