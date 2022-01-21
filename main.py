from settings.server import server_manager
from routers import setters, webhook

app = server_manager.get_app()

app.include_router(setters.api)
app.include_router(webhook.api)
