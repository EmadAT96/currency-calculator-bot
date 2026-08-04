from dataclasses import dataclass
from typing import Any

class ExchangeResponse:

    success: bool

    data: Any = None

    error: str | None = None


@dataclass
class CurrencyRate:
    base: str
    target: str
    rate: float
    name: str