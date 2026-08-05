from exhange_rate.config.provider_config_repository import ProviderConfigRepository
from exhange_rate.factory.auth_factory import AuthFactory
from exhange_rate.factory.provider_factory import ProviderFactory
from exhange_rate.core.request_builder import RequestBuilder

class ExchangeRateService:

    def __init__(
        self,
        exhange_provider_name: str
    ):

        self.provider_name = exhange_provider_name
        

    def get_exchange_rates(self):

        config = ProviderConfigRepository.get(
            self.provider_name
        )

        auth = AuthFactory.create(
            config.auth
        )

        request = RequestBuilder.build(
            config
        )

        provider = ProviderFactory.create(
            self.provider_name,
            request,
            auth
        )

        result = provider.get_rates()

        return result

