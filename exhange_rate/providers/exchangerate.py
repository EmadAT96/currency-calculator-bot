from exhange_rate.mappers.exchangerate import ExchangeMapper
from exhange_rate.validators.exchangerate import ExchangeValidator
from exhange_rate.contracts.provider import ExchangeRateProvider
from exhange_rate.registry.provider_registry import register_provider

@register_provider(
    "exchange_rate",
    ExchangeMapper,
    ExchangeValidator
)
class ExchangeProvider(ExchangeRateProvider):
    def get_rates(self):
        self.auth_strategy.apply(self.request_config)
        
        response = self.http.send(self.request_config)

        response.raise_for_status()

        data = response.json()

        data = self.validator.validate(data)

        return self.mapper.transform(data)