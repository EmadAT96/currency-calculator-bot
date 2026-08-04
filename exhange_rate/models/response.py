from dataclasses import dataclass, field
from typing import Any
from datetime import datetime

class ExchangeResponse:

    success: bool

    data: Any = None

    error: str | None = None


@dataclass
class CurrencyRate:
    name: str
    value: str
    change: float | None = None
    date: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    