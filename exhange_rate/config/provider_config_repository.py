import os

from dotenv import load_dotenv

from exhange_rate.models.provider_config import ProviderConfig
from exhange_rate.models.base_config import HttpMethod

from exhange_rate.providers.navasan import NavasanProvider
from exhange_rate.mappers.navasan import NavasanMapper
from exhange_rate.providers.brsap import BrsapProvider
from exhange_rate.mappers.brsap import BrsapMapper
from exhange_rate.mappers.exchangerate import ExchangeMapper
from exhange_rate.providers.exchangerate import ExchangeProvider

load_dotenv()
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
                "value":os.getenv("BRSAPI_TOKEN")
            }
        ),
        "navasan": ProviderConfig(
            "navasan",
            url="http://api.navasan.tech/latest/",
            auth={
                "type":"query_param",
                "key_name":"api_key",
                "value":os.getenv("NAVASAN_TOKEN")
            }
        ),
        "exchange_rate": ProviderConfig(
            "exchange_rate",
            url="https://api.exchangerate.host/live",
            auth={
                "type":"query_param",
                "key_name":"access_key",
                "value":os.getenv("EXCHANGE_TOKEN")
            },
            query_params={
                "source":"IRR"
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