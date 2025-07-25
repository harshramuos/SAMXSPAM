import logging
from telethon import TelegramClient
from os import getenv
from KapilYadav.data import ALTRON

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# VALUES REQUIRED FOR XBOTS
API_ID = "299988"
API_HASH = "fde39a821ea6aba52b4b36b2e205"

CMD_HNDLR = getenv("CMD_HNDLR", default=".")
hl = CMD_HNDLR  # This fixes the import issue in bot.py

 # Bot Tokens
BOT_TOKEN ="7990740130:Ac6ezEQc0qbJZRSH5eb3oFkc"
BOT_TOKEN2 = "7916510:AAE6l3HdlRFlqilOdg3xyPlFNQb2N3rurxFI"
BOT_TOKEN3 = "7967278498:AAGBkxII-Bd65or98BOlqbpZgXoR7FKW2tE"
BOT_TOKEN4 = "7667898132:AAGM4J9CJTdCNwhtjhFDLKGyNGlkQdm3Rfg"
BOT_TOKEN5 = "765677769:AHmR6tVkhi8fh9Tl-xYY5KT1_TTk"
BOT_TOKEN6 = "8109721665:"hhshhdhdhs"
BOT_TOKEN7 = "7634103299:AYc72RvRDBQtC0f-Wq1Kgghrrs"
BOT_TOKEN8 = "7660893693:AAvkLQcVMUWC8vMD3QctM9BG8yD9m0"
BOT_TOKEN9 = "8168299777:AAukFLp2zpmSdJTbHU-pWsuIjQxJg"
BOT_TOKEN10 = "8079640351ayaZJOqz73X10CnU2baBCzai3XNhg"

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6219473300").split()))
for x in ALTRON:
    SUDO_USERS.append(x)

OWNER_ID = int(getenv("OWNER_ID", default="5968988297"))
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
