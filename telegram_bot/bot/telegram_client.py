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

    