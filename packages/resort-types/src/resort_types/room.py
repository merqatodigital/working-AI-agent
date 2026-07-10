from pydantic import BaseModel, Field


class Room(BaseModel):
    id: str
    room_number: str
    room_type: str = "standard"
    floor: int = 1
    status: str = "available"
    base_rate: float = 0.0
    current_rate: float | None = None
    amenities: list[str] = Field(default_factory=list)
    last_cleaned_at: str | None = None
    maintenance_notes: str | None = None

    @property
    def effective_rate(self) -> float:
        return self.current_rate if self.current_rate is not None else self.base_rate
