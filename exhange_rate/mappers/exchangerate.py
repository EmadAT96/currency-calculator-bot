from exhange_rate.contracts.mapper import ResponseMapper
from exhange_rate.models.response import CurrencyRate
from datetime import datetime

class ExchangeMapper(ResponseMapper):

    def transform(self, data):

        results = []

        timestamp = data["timestamp"]
        dt_object = datetime.fromtimestamp(timestamp)

        for name, item in data["quotes"].items():
            results.append(
                CurrencyRate(
                    name=name,
                    value= int(1 / item),
                    change=0,
                    date=dt_object.strftime("%Y-%m-%d %H:%M:%S")
                )
            )
        return results