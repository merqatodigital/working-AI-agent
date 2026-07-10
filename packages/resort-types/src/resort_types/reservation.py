from pydantic import BaseModel, Field


class Reservation(BaseModel):
    id: str
    guest_id: str
    room_id: str | None = None
    check_in_date: str
    check_out_date: str
    status: str = "confirmed"
    room_type: str = "standard"
    adults: int = 1
    children: int = 0
    total_amount: float = 0.0
    paid_amount: float = 0.0
    notes: str | None = None

    @property
    def balance_due(self) -> float:
        return self.total_amount - self.paid_amount

    @property
    def nights(self) -> int:
        from datetime import date

        ci = date.fromisoformat(self.check_in_date)
        co = date.fromisoformat(self.check_out_date)
        return (co - ci).days


class BookingProposal(BaseModel):
    guest_id: str
    room_type: str
    check_in_date: str
    check_out_date: str
    adults: int = 1
    children: int = 0
    special_requests: str | None = None
    proposed_rate: float | None = None
    notes: str | None = None
