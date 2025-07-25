# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     ⚙️ CONFIGURATION FILE | Powered By @ItsKapilYadav 
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import os
import logging
from telethon import TelegramClient
from dotenv import load_dotenv
from KapilYadav.data import ALTRON

# Load from .env file if present (works on VPS)
load_dotenv()

# Logger setup
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# Required values
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

CMD_HNDLR = os.getenv("CMD_HNDLR", default=".")
hl = CMD_HNDLR

# Bot Tokens
BOT_TOKEN_LIST = [os.getenv(f"BOT_TOKEN{i}", "") for i in range(1, 11)]

# Sudo Users
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "5968988297").split()))
for x in ALTRON:
    SUDO_USERS.append(x)

OWNER_ID = int(os.getenv("OWNER_ID", "5968988297"))
SUDO_USERS.append(OWNER_ID)

# Initialize clients
CLIENTS = []
for i, token in enumerate(BOT_TOKEN_LIST):
    if token:  # Only initialize if token is present
        client = TelegramClient(f'X{i+1}', API_ID, API_HASH).start(bot_token=token)
        CLIENTS.append(client)

# Optional: assign first 10 clients individually for backward compatibility
X1 = CLIENTS[0] if len(CLIENTS) > 0 else None
X2 = CLIENTS[1] if len(CLIENTS) > 1 else None
X3 = CLIENTS[2] if len(CLIENTS) > 2 else None
X4 = CLIENTS[3] if len(CLIENTS) > 3 else None
X5 = CLIENTS[4] if len(CLIENTS) > 4 else None
X6 = CLIENTS[5] if len(CLIENTS) > 5 else None
X7 = CLIENTS[6] if len(CLIENTS) > 6 else None
X8 = CLIENTS[7] if len(CLIENTS) > 7 else None
X9 = CLIENTS[8] if len(CLIENTS) > 8 else None
X10 = CLIENTS[9] if len(CLIENTS) > 9 else None

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     ✅ CONFIG LOADED SUCCESSFULLY | Designed By @ItsKapilYadav
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
