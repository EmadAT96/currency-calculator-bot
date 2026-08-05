from exhange_rate.models.request import RequestConfig

class RequestBuilder:

    @staticmethod
    def build(config):

        return RequestConfig(

            url=config.url,

            method=config.method,

            headers=config.headers,

            query_params=config.query_params,

            payload=config.payload,

            timeout=config.timeout

        )