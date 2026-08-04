
from auth.api_key import ApiKeyHeaderAuth
from auth.query_param import QueryParamsAuth
from auth.oauth2 import OAuth2Auth

class AuthFactory:

    auths = {

        "api_key_header": ApiKeyHeaderAuth,

        "query_param": QueryParamsAuth,

        "oauth_header": OAuth2Auth

    }

    @classmethod
    def create(cls, config):

        if not config:
            return None

        auth_class = cls.auths.get(
            config["type"]
        )

        if not auth_class:
            raise ValueError(
                "Auth type not supported"
            )

        return auth_class(
            **config
        )