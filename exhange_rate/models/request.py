from dataclasses import dataclass, field
from typing import Any
from exhange_rate.models.base_config import HttpMethod

@dataclass
class RequestConfig:

    url: str

    method: str = HttpMethod.GET

    headers: dict[str, str] = field(
        default_factory=dict
    )

    query_params: dict[str, Any] = field(
        default_factory=dict
    )

    payload: dict | None = None

    timeout: int = 10 

    def __post_init__(self):

        if not self.url:
            raise ValueError(
                "Url is required"
            )

        if self.timeout <= 0:
            raise ValueError(
                "Timeout must be positive number"
            )