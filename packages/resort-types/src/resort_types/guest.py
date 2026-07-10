from pydantic import BaseModel, Field


class GuestPreferences(BaseModel):
    room_view: str | None = None
    dietary: str | None = None
    pillow: str | None = None
    quiet_room: bool | None = None
    late_checkout: bool | None = None
    language: str | None = None
    adventure_activities: bool | None = None


class GuestProfile(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str | None = None
    phone: str | None = None
    nationality: str | None = None
    preferences: GuestPreferences = Field(default_factory=GuestPreferences)
    past_stays: list[dict] = Field(default_factory=list)
    loyalty_tier: str = "standard"
    notes: str | None = None

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class GuestRequest(BaseModel):
    id: str
    guest_id: str
    reservation_id: str | None = None
    request_type: str
    description: str
    priority: str = "normal"
    department: str | None = None
    status: str = "open"
    created_at: str | None = None
