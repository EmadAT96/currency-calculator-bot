from exhange_rate.contracts.mapper import ResponseMapper
from exhange_rate.models.response import CurrencyRate

class NavasanMapper(ResponseMapper):

    def transform(self, data):

        results = []

        for name, item in data.items():
            print(item)
            results.append(
                CurrencyRate(
                    name=name,
                    value=item.get("value",""),
                    change=item.get("change",0),
                    date=item["date"]
                )
            )
        return results