import asyncio
from datetime import datetime
from telethon import events
from telethon.errors import ForbiddenError
from config import OWNER_ID, SUDO_USERS
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

LOG_FILE = "KapilYadavLogs.txt"

clients = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

for client in clients:
    @client.on(events.NewMessage(pattern=r"\.logs(?: |$)(.*)"))
    async def logs(event):
        if event.sender_id != OWNER_ID:
            return await event.reply("» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")

        try:
            start = datetime.now()
            fetch = await event.reply("__Fetching Logs...__")

            # Simulate log data (replace with actual log reading if needed)
            logs = "⚡ Kapil Yadav Bot Logs ⚡\n\nThis is a placeholder for actual logs."

            with open(LOG_FILE, "w") as logfile:
                logfile.write(logs)

            await asyncio.sleep(1)

            await client.send_file(
                event.chat_id,
                LOG_FILE,
                caption=f"⚡ **Kapil Yadav Logs** ⚡\n » **Time Taken:** `{(datetime.now() - start).seconds} seconds`"
            )
            await fetch.delete()

        except Exception as e:
            await event.reply(f"An error occurred:\n\n`{str(e)}`")
