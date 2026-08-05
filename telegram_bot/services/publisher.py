from telegram_bot.formatters.currency_formatter import CurrencyFormatter

class CurrencyPublisher:
    IMPORTANT_RATES = {
        "usd_usdt",
        "sekkeh",
        "bahar",
        "nim",
        "rob",
        "abshodeh",
        "gerami",
        "usd_buy",
        "dirham_dubai",
        "eur_hav",
        "gbp_hav"
    }

    def __init__(
        self,
        exchange_rate_service,
        telegram_client,
        chat_id
    ):
        self.exchange_rate_service = exchange_rate_service
        self.telegram_client = telegram_client
        self.chat_id = chat_id

    async def publish(self):

        rates = self.exchange_rate_service.get_exchange_rates()

        selected_rates = [
            rate
            for rate in rates
            if rate.name in self.IMPORTANT_RATES
        ]

        message = CurrencyFormatter.format_rates(
            selected_rates
        )

        await self.telegram_client.send_message(
            self.chat_id,
            message
        )