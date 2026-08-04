from config.provider_config_repository import ProviderConfigRepository
from factory.auth_factory import AuthFactory
from factory.provider_factory import ProviderFactory
from core.request_builder import RequestBuilder
from providers.brsap import BrsapProvider

provider_name = "brsap"

config = ProviderConfigRepository.get(
    provider_name
)

auth = AuthFactory.create(
    config.auth
)

request = RequestBuilder.build(
    config
)

provider = ProviderFactory.create(
    provider_name,
    request,
    auth
)

result = provider.get_rates()

print(result)