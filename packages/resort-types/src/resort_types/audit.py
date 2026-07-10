from pydantic import BaseModel, Field


class AuditEntry(BaseModel):
    id: str
    action: str
    department: str | None = None
    agent_step: str | None = None
    details: dict = Field(default_factory=dict)
    guest_id: str | None = None
    reservation_id: str | None = None
    staff_id: str | None = None
    task_id: str | None = None
    created_at: str | None = None


class ManagerBrief(BaseModel):
    date: str
    occupancy_rate: float = 0.0
    guests_checked_in: int = 0
    arrivals_today: int = 0
    departures_today: int = 0
    open_tasks: int = 0
    urgent_tasks: int = 0
    pending_approvals: int = 0
    low_stock_items: int = 0
    recent_issues: list[str] = Field(default_factory=list)
    agent_actions_today: int = 0
