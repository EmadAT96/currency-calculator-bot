from abc import ABC, abstractmethod

class ExchangeRateProvider(ABC):

    def __init__(
        self,
        request_config,
        auth_strategy,
        mapper,
        validator,
        http_client,
    ):

        self.request_config = request_config
        self.auth_strategy = auth_strategy
        self.mapper = mapper
        self.validator = validator
        self.http = http_client        

    @abstractmethod
    def get_rates(self):
        pass