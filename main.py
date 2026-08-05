import asyncio
from telegram_bot.bot.telegram_client import TelegramClient
from telegram_bot.services.publisher import CurrencyPublisher

from telegram_bot.services.exchange_rate_service import ExchangeRateService

async def main():

    exchange_service = ExchangeRateService(
        "navasan"
    )

    telegram_client = TelegramClient(
        token="8634927023:AAHFae9lPTHAjVKWs1WED-_S4M-15k_YTuA"
    )

    updates = await telegram_client.bot.get_updates()

    for update in updates:

        publisher = CurrencyPublisher(
            exchange_rate_service=exchange_service,
            telegram_client=telegram_client,
            chat_id=update.effective_chat.id
        )

        await publisher.publish

if __name__ == "__main__":
    asyncio.run(main())