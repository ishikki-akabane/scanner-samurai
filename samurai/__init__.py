import logging
import time

from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import MemorySession

#===================================
API_HASH = "78ba6352dd5cdc166fdef5aa84ba7c67"
API_ID = 7217645
BOT_TOKEN = "5137683296:AAHHib5JAImz2bCEuOD_5PPPXbesf5kSzho"
SESSION_STRING = "BQBNYYmK_Ze0A1qWCGVJKMVVImH2w1lo8VXCfIfK1w85Y9g3tr4Ia9crvB9yGW7kPl6BskYDm7XvvJystcOBnzZ1vIdAk2hlEsU8wuMwUD2WQlTaDD_8eGBSv_iZbXT8BobuuRNhrc_5WF4h2Ae7Ojz1ukLdMfMmLkbELFMTcVbxgwkhlmEPTF35baeK1K9xNXK8ipaugQt4Xsh3KYKpitQcRF5jrsfFGhtGgHnIER2oD3AixjebigCtaPgCPd9PqwY6ByEzlaj0C9r29o0J3sdfRdxNhDqe8l7FHsHrjwuTVl-WAbpltkZQtMoSf84_ChRboWdRI969WqxSmotAocKwAAAAAVYVPZwA"

SUPPORT_CHAT = "https://t.me/RONIN_Fighters_Fd"
SUPPORT_ID = -1001553284045
GBAN_CHANNEL_ID = -1001833557507
SPAM_GROUP = -1001833557507
FBAN_SPAM = -1001833557507


DOWNLOAD_DIRECTORY = "./"

OWNER_ID = [5030730429 1793699293]
SUDOLIST = [] #Enforcers
SUPPORTLIST = [] #Inspectors
DEV_LIST = []

DEV_USERS = DEV_LIST + OWNER_ID
SUDO_USERS = SUDOLIST + DEV_USERS #Enforcers
SUPPORT_USERS = SUPPORTLIST + SUDO_USERS #Inspectors


REQUEST_IMG = "https://telegra.ph/file/9ed4c2423cb907046f254.jpg"

MONGO_DB = "mongodb+srv://DARKAMAN:DARKAMAN@cluster0.snqhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
#===================================

StartTime = time.time()

# enable logging
FORMAT = "[SAMURAI] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger('ptbcontrib.postgres_persistence.postgrespersistence').setLevel(logging.WARNING)

LOGGER = logging.getLogger('[SAMURAI]')
LOGGER.info("SAMURAI Scanner is starting...")
LOGGER.info("Handled by: IShIkkI AKABANE")


pbot = Client("samurai", API_ID, API_HASH, bot_token=BOT_TOKEN)
ubot = Client("Client", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)


pbot.start()
ubot.start()

bot = pbot.get_me()
BOT_ID = bot.id
if bot.last_name:
    BOT_NAME = bot.first_name + " " + bot.last_name
else:
    BOT_NAME = bot.first_name
BOT_USERNAME = bot.username


tbot = TelegramClient(MemorySession(), API_ID, API_HASH)
