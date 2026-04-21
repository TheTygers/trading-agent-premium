from pydantic import BaseModel
from typing import Literal


class AgentStatus(BaseModel):
    running: bool = False
    cycle: int = 0
    health: Literal["healthy", "stopped"] = "stopped"
    message: str = "idle"


class AgentConfig(BaseModel):
    mode: str = "paper"
    symbols: list[str] = ["BTCUSDT", "ETHUSDT"]
    active_allocation_pct: float = 0.35


class AccountState(BaseModel):
    portfolio_total_lei: float = 1000.0
    active_capital_lei: float = 350.0
    available_cash_lei: float = 350.0
    equity_lei: float = 350.0