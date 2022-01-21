from enum import Enum

class Action(Enum):
    SET_WEBHOOK = "setWebhook"
    GET_WEBHOOK = "getWebhook"
    SEND_MESSAGE = "sendMessage"
    
    def __str__(self):
        return str(self.value)
        