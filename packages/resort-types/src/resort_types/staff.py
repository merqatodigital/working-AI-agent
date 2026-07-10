from pydantic import BaseModel, Field


class Staff(BaseModel):
    id: str
    first_name: str
    last_name: str
    role: str
    department: str
    email: str | None = None
    phone: str | None = None
    shift_schedule: dict = Field(default_factory=dict)
    is_active: bool = True
    hire_date: str | None = None

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Task(BaseModel):
    id: str
    department: str
    title: str
    description: str = ""
    priority: str = "normal"
    status: str = "pending"
    assigned_to: str | None = None
    room_id: str | None = None
    guest_id: str | None = None
    reservation_id: str | None = None
    created_at: str | None = None
    started_at: str | None = None
    completed_at: str | None = None
    completion_notes: str | None = None
    created_by: str = "agent"


class Shift(BaseModel):
    staff_id: str
    shift_start: str
    shift_end: str
    department: str
    role: str
