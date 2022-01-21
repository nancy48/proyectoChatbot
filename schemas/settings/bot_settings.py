import os
from pydantic import BaseSettings

class SettingsManager(BaseSettings):
    TOKEN: str = os.environ.get("TOKEN")
    API_URL: str = f"https://api.telegram.org/bot{TOKEN}/%s"

BotSettings = SettingsManager()
