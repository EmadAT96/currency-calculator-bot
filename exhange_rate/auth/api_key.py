from exhange_rate.contracts.auth import AuthStrategy
class ApiKeyHeaderAuth(AuthStrategy):

    def __init__(
            self,
            key,
            **kwargs
        ):
        self.key = key

    def apply(self, request_config):

        request_config.headers = {
            **request_config.headers,
            "X-API-KEY": self.key
        }