from pydantic import BaseModel, Field


class StockItem(BaseModel):
    id: str
    item_name: str
    category: str
    current_quantity: int = 0
    min_quantity: int = 10
    unit: str = "units"
    unit_cost: float = 0.0
    supplier: str | None = None
    last_restocked_at: str | None = None

    @property
    def is_low(self) -> bool:
        return self.current_quantity <= self.min_quantity

    @property
    def stock_value(self) -> float:
        return self.current_quantity * self.unit_cost


class StockMovement(BaseModel):
    item_id: str
    quantity: int
    movement_type: str  # "in", "out", "adjustment"
    reason: str
    recorded_by: str = "agent"
