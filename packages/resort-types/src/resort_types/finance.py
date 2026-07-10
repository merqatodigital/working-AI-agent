from pydantic import BaseModel, Field


class Transaction(BaseModel):
    id: str
    transaction_type: str  # "income", "expense"
    category: str
    amount: float
    description: str
    reference_id: str | None = None
    recorded_by: str = "agent"
    created_at: str | None = None


class ExpenseProposal(BaseModel):
    description: str
    amount: float
    category: str
    vendor: str | None = None
    justification: str | None = None
    requested_by: str = "agent"


class FinancialSummary(BaseModel):
    total_income: float = 0.0
    total_expenses: float = 0.0
    net_profit: float = 0.0
    occupancy_rate: float = 0.0
    avg_daily_rate: float = 0.0
    revpar: float = 0.0
    pending_receivables: float = 0.0
    unpaid_balances: list[dict] = Field(default_factory=list)
