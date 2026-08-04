from contracts.provider import ExchangeRateProvider
from registry.provider_registry import register_provider
from mappers.brsap import BrsapMapper
from validators.brsap import BrsapValidator

@register_provider(
    "brsap",
    BrsapMapper,
    BrsapValidator
)
class BrsapProvider(ExchangeRateProvider):
    def get_rates(self):

        self.auth_strategy.apply(self.request_config)

        response = self.http.send(self.request_config)

        response.raise_for_status()

        data = response.json()

        data = self.validator.validate(data)

        return self.mapper.transform(data)