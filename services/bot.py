import httpx
from json import loads
from typing import Tuple, Union
from schemas.settings.bot_settings import BotSettings
from schemas.enums.actions import Action

class BotService:
    
    @classmethod
    async def setWebhook(cls, webhook_url: str) -> Tuple:
        async with httpx.AsyncClient() as client:
            url = BotSettings.API_URL % Action.SET_WEBHOOK  # le indicamos que accion queremos realizar
            response = await client.post(url=url, json={"url": webhook_url})
        return loads(response.content), response.status_code

    @classmethod
    async def reply_message(cls, chat_id: Union[str, int], text: str) -> Tuple:
        async with httpx.AsyncClient() as client:
            url = BotSettings.API_URL % Action.SEND_MESSAGE
            response = await client.post(url=url, json={"chat_id": chat_id, "text": text})
        return loads(response.content), response.status_code

