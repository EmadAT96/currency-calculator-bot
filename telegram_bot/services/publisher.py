from telegram_bot.formatters.currency_formatter import CurrencyFormatter
from telegram_bot.generators.currency_image_generator import CurrencyImageGenerator

from datetime import datetime

class CurrencyPublisher:
    IMPORTANT_RATES = {
        "IRRUSD",
        "IRRTRY",
        "IRREUR",
        "IRRCAD",
        "IRRAED",
        "IRRGBP"
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
        
        image = CurrencyImageGenerator(
            '../templates/currency_template.png',
            '../fonts/Vazirmatn-Bold.ttf'
        )
        
        output = image.generate(
            selected_rates,
            output_path='../output/result.png'
        )
        
        await self.telegram_client.send_photo(            
            self.chat_id,
            output,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )