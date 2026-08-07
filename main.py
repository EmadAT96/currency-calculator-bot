import asyncio
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from dotenv import load_dotenv

from telegram_bot.bot.telegram_client import TelegramClient
from telegram_bot.services.publisher import CurrencyPublisher
from telegram_bot.services.exchange_rate_service import ExchangeRateService

load_dotenv()

async def job():
    
    exchange_service = ExchangeRateService(
        "exchange_rate"
    )

    telegram_client = TelegramClient(
        token=os.getenv("TELEGRAM_BOT_TOKEN")
    )

    updates = await telegram_client.bot.get_updates()
    
    print(updates)

    for update in updates:
        
        print(update.effective_chat.id)
        
        publisher = CurrencyPublisher(
            exchange_rate_service=exchange_service,
            telegram_client=telegram_client,
            chat_id=update.effective_chat.id
        )

        await publisher.publish()
        
        

async def main():
            
    scheduler = AsyncIOScheduler()

    scheduler.add_job(job, IntervalTrigger(minutes=5))

    scheduler.start()
    
    await asyncio.Event().wait()
    
if __name__ == "__main__":
    asyncio.run(main())