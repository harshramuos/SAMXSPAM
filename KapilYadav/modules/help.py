from telethon import events, Button
import asyncio
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl

clients = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

HELP_STRING = (
    "\n💥 <b>𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨</b> 💥\n\n"
    "⚙️ Click a button below to view commands.\n"
    "🔧 <b>Developer:</b> <a href='https://t.me/ItsKapilYadav'>@ItsKapilYadav</a>"
)

HELP_BUTTON = [
    [Button.inline("💣 SPAM", data=b"spam"), Button.inline("☠ RAID", data=b"raid")],
    [Button.inline("👥 GROUP", data=b"group"), Button.inline("✨ EXTRA", data=b"extra")],
    [
        Button.url("📢 CHANNEL", "https://t.me/KomalMusicRobotChannel"),
        Button.url("🛠 SUPPORT", "https://t.me/KomalMusicRobotSupport"),
    ],
]

# Messages
extra_msg = f"""<b>✨ EXTRA COMMANDS</b>\n\n<code>{hl}ping</code> - Check ping
<code>{hl}reboot</code> - Restart bot
<code>{hl}sudo</code> - Add sudo
<code>{hl}logs</code> - Show logs
<code>{hl}alive</code> - Show alive message
<code>{hl}echo</code> - Echo reply
<code>{hl}rmecho</code> - Remove echo
<code>{hl}leave</code> - Leave group
<code>{hl}setwelcome</code> - Set welcome msg
<code>{hl}setleave</code> - Set leave msg
<code>{hl}rules</code> - Show rules

© @ItsKapilYadav"""

raid_msg = f"""<b>☠ RAID COMMANDS</b>\n\n<code>{hl}raid</code> - Start raid
<code>{hl}rraid</code> - Reply raid
<code>{hl}drraid</code> - D reply raid
<code>{hl}mraid</code> - Multi raid
<code>{hl}sraid</code> - Super raid
<code>{hl}craid</code> - Combo raid

© @ItsKapilYadav"""

spam_msg = f"""<b>💣 SPAM COMMANDS</b>\n\n<code>{hl}spam</code> - Start spam
<code>{hl}pspam</code> - Porn spam
<code>{hl}hang</code> - Hang command

© @ItsKapilYadav"""

group_msg = f"""<b>👥 GROUP COMMANDS</b>\n\n<code>{hl}promote</code> | <code>{hl}demote</code>
<code>{hl}ban</code> | <code>{hl}unban</code>
<code>{hl}kick</code> | <code>{hl}mute</code>
<code>{hl}warn</code> | <code>{hl}unwarn</code>
<code>{hl}lock</code> | <code>{hl}unlock</code>
<code>{hl}setwelcome</code> | <code>{hl}setleave</code>
<code>{hl}setrules</code> | <code>{hl}rules</code>

Auto messages will be sent on join/leave.

© @ItsKapilYadav"""

# Button map
button_map = {
    "help_back": HELP_STRING,
    "spam": spam_msg,
    "raid": raid_msg,
    "extra": extra_msg,
    "group": group_msg,
}

# Help command
async def help_handler(event):
    if event.sender_id in SUDO_USERS:
        await event.reply(HELP_STRING, buttons=HELP_BUTTON, parse_mode="html")

# Callback event
def generate_cb(pattern, msg):
    async def cb(event):
        if event.query.user_id not in SUDO_USERS:
            return await event.answer("🚫 Access Denied!", alert=True)
        try:
            old = (await event.get_message()).message.strip()
            if msg.strip() == old:
                return await event.answer("⛔ Already on this menu.", alert=True)
            await event.edit(
                msg,
                buttons=[[Button.inline("⬅ Back", data=b"help_back")]] if pattern != "help_back" else HELP_BUTTON,
                parse_mode="html"
            )
            await asyncio.sleep(0.3)  # Prevent floodwait
        except Exception as e:
            if "MessageNotModified" not in str(e):
                await event.answer(f"❌ Error:\n{e}", alert=True)
    return cb

# Register on all clients
for client in clients:
    client.add_event_handler(help_handler, events.NewMessage(pattern=fr"\{hl}help(?: |$)(.*)"))
    for pattern, msg in button_map.items():
        client.add_event_handler(generate_cb(pattern, msg), events.CallbackQuery(data=pattern.encode()))