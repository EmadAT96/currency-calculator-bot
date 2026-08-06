from telegram import Bot

class TelegramClient:

    def __init__(
        self,
        token: str
    ):

        self.bot = Bot(token)

    async def send_message(
        self,
        chat_id,
        text
    ):
        await self.bot.send_message(
            chat_id=chat_id,
            text=text
        )
        
    async def send_photo(
        self,
        chat_id,
        image,
        caption=""
    ):
        await self.bot.send_photo(            
            chat_id=chat_id,
            photo=image,
            caption=caption
        )

    