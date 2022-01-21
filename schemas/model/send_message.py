from pydantic import BaseModel, Field
from typing import Union

class SendMessageSchema(BaseModel):
    chat_id: Union[int, str] = Field(..., title="ID del usuario o chat")
    text: str = Field(..., title="Cuerpo del mensaje")

    class Config:
        schema_extra = {
            "example": {
                "chat_id": "1084783282",
                "text": "Hola!"
            }
        }