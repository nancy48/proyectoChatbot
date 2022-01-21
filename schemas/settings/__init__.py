from xmlrpc import server
from settings.server import server_manager
from dotenv import load_dotenv
import os

if server_manager.get_app().debug:
    load_dotenv(os.path.abspath(__file__).replace("__init__.py", ".env"))
