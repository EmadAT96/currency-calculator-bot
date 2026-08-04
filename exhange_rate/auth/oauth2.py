from contracts.auth import AuthStrategy

class OAuth2Auth(AuthStrategy):

    def __init__(
            self,
            access_token: str,
            refresh_token: str = None,
            refresh_url: str = None,
            **kwargs
        ):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.refresh_url = refresh_url

    def apply(self, request_config):
        request_config.headers["Authorization"] = f"Bearer {self.access_token}"

    def refresh(self):
        if not self.refresh_url or not self.refresh_token:
            raise ValueError("No Refresh token or url available")

        pass
    
        