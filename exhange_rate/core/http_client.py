import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from exhange_rate.exceptions.provider import ProviderTimeoutExeption

class HttpClient:

    def __init__(self):
        self.session = requests.Session()

        retry = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[
                500,
                502,
                503,
                504
            ]
        )

        adapter = HTTPAdapter(
            max_retries=retry
        )

        self.session.mount(
            "http://",
            adapter
        )

        self.session.mount(
            "https://",
            adapter
        )

    def send(self, config):

        try:
            return self.session.request(
                method=config.method.value,
                url=config.url,
                headers=config.headers,
                params=config.query_params,
                json=config.payload,
                timeout=config.timeout
            )
        except requests.Timeout:

            raise ProviderTimeoutExeption(
                "Provider timeout"
            )