# ©️biisal jai shree krishna 😎
from os import environ
from dotenv import load_dotenv

load_dotenv()

API_ID = environ.get("API_ID" , "20901045")
API_HASH = environ.get("API_HASH" , "dec03cafafbd892b285499762a896082")
BOT_TOKEN = environ.get("BOT_TOKEN" , "2099007:AAH1b3d7b3b1b3d7b3b1b3d7b3b1b3d7b3")
ADMIN = int(environ.get("ADMIN" , "6324457826"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1002473045711"))
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002447343432")
MONGO_URL = environ.get("MONGO_URL" , "mongodb+srv://Alone:Sofihub76@cluster0.3bfyy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1002199891363")
)
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
