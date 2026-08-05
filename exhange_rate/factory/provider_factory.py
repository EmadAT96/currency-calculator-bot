from exhange_rate.core.http_client import HttpClient
from exhange_rate.registry.provider_registry import ProviderRegistry

class ProviderFactory:

    http_client = HttpClient()

    @classmethod
    def create(
        cls,
        provider_name: str,
        request_config, 
        auth_strategy,
    ):

        config = ProviderRegistry.get(
            provider_name
        )

        return config["provider_class"](
            request_config=request_config,
            auth_strategy=auth_strategy,
            mapper=config["mapper_class"](),
            validator=config["validator_class"](),
            http_client=cls.http_client
        )