from contracts.mapper import ResponseMapper
from models.response import CurrencyRate

class BrsapMapper(ResponseMapper):

    def transform(self, data):

        if isinstance(data, list):
            
            return [
                self._map_item(item)
                for item in data
            ]

        return self._map_item(data)

    def _map_item(self, item):

        return CurrencyRate(
            base=item["l18"],
            target=item["pmin"],
            rate=float(item["pmax"]),
            name=item["l30"]
        )