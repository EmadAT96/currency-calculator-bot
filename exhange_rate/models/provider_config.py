from dataclasses import dataclass, field
from exhange_rate.models.base_config import HttpMethod

@dataclass
class ProviderConfig:
    name: str
    
    url: str

    method: HttpMethod = HttpMethod.GET

    headers: dict = field(
        default_factory=dict
    )

    query_params: dict = field(
        default_factory=dict
    )

    payload: dict | None = None

    timeout: int = 10

    auth: dict | None = None

    def __post_init__(self):
    
        if not self.url:
            raise ValueError(
                "Url is required"
            )

        if self.timeout <= 0:
            raise ValueError(
                "Timeout must be positive number"
            )