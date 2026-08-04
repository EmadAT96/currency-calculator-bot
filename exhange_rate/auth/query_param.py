from contracts.auth import AuthStrategy

class QueryParamsAuth(AuthStrategy):

    def __init__(
            self,
            key_name: str,
            value: str,
            **kwargs
        ):
        self.key_name = key_name
        self.value = value

    def apply(self, request_config):
        request_config.query_params[self.key_name] = self.value