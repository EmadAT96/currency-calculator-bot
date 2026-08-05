from exhange_rate.mappers.navasan import NavasanMapper
from exhange_rate.validators.navasan import NavasanValidator
from exhange_rate.contracts.provider import ExchangeRateProvider
from exhange_rate.registry.provider_registry import register_provider

@register_provider(
    "navasan",
    NavasanMapper,
    NavasanValidator
)
class NavasanProvider(ExchangeRateProvider):
    def get_rates(self):
        self.auth_strategy.apply(self.request_config)
        
        response = self.http.send(self.request_config)

        response.raise_for_status()

        data = response.json()

        data = self.validator.validate(data)

        return self.mapper.transform(data)