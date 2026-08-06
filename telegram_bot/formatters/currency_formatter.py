class CurrencyFormatter:

    @staticmethod
    def format_rates(rates):

        lines = [
            "📊 گزارش نرخ ارز",
            ""
        ]

        for rate in rates:

            change_icon =  "🔺"

            if rate.change is not None and rate.change < 0:
                change_icon = "🔻"

            lines.extend([
                f"💱 {rate.name}",
                f"💰 قیمت: {rate.value}",
                f"{change_icon} تغییر: {rate.change}",
                ""
            ])


        return "\n".join(lines)