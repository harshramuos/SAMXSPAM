import logging
from telethon import TelegramClient
from os import getenv
from KapilYadav.data import ALTRON

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# VALUES REQUIRED FOR XBOTS
API_ID = "27203"
API_HASH = "2d5aec15f1e703a217245b30cb8"

CMD_HNDLR = getenv("CMD_HNDLR", default=".")
hl = CMD_HNDLR  # This fixes the import issue in bot.py

 # Bot Tokens
BOT_TOKEN = "7588691860:AAGx_nLnMiBwMS1AO_eo11UTgfrLkU"
BOT_TOKEN2 = "7672872618:AOHAT32hcn-dsFNSV2X57FiiWhUAnJ5I"
BOT_TOKEN3 = "7716554217:AAOGWk_exXGCfu50TToNnhh1J2Qf4"
BOT_TOKEN4 = "7974842321:AAFHFzxqpKZ-tJZ40BxHILyhPV9Ti5c4"
BOT_TOKEN5 = "7997284718:AAksmeq5AAbJrSpFJaDLrDBkcpdhM"
BOT_TOKEN6 = "7639081689:AAEFNRPwbO7vhFWOoJtMzzaPN8owEBm0"
BOT_TOKEN7 = "7258168624:Axm9fHozLfMw0aCLp_ezMLuqGhaW4w"
BOT_TOKEN8 = "7643330995:AAFTM9HW38Hsj7hfL8KoSa6ckVx5oXws"
BOT_TOKEN9 = "7336955695:AAJPm3Ga6y7ibD5GUeO7A4H5sWVVhJnU"
BOT_TOKEN10 = "7639081689:AAENNRPwb7uvhFWOoJtMzzaPN8owEBm0"
SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="5968988297").split()))
for x in ALTRON:
    SUDO_USERS.append(x)

OWNER_ID = int(getenv("OWNER_ID", default="7774742430"))
SUDO_USERS.append(OWNER_ID)

# ------------- CLIENTS -------------
X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
