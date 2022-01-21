from pydantic import BaseModel, Field, HttpUrl


class SetWebhookSchema(BaseModel):
    url: HttpUrl = Field(..., title="URL del Webhook")

    class Config:
        schema_extra = {
            "example": {
                "url": "https://www.misitioweb.com/api/v1/webhook/",
            }
        }
