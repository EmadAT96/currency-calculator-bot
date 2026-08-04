from models.provider_config import ProviderConfig
from models.base_config import HttpMethod

class ProviderConfigRepository:

    configs = {
        "brsap": ProviderConfig(
            name="brsap",
            url="https://Api.BrsApi.ir/Tsetmc/AllSymbols.php",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/106.0.0.0"
            },
            auth={
                "type":"query_param",
                "key_name":"key",
                "value":"BNeKH7naELKszrLWD42pr9juKsJG3t3w"
            }
        ),
        "navasan": ProviderConfig(
            "navasan",
            url="http://api.navasan.tech/latest/",
            auth={
                "type":"query_param",
                "key_name":"api_key",
                "value":"freenx5KrlKZ3oZb4bknlAIQIGRuEARF"
            }
        )
    }

    @classmethod
    def get(cls, name):
        if name not in cls.configs:
            raise ValueError(
                f"config {name} not found"
            )

        return cls.configs[name]