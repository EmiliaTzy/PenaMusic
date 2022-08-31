from Zaid.config import LOG_GROUP_ID
from Zaid.MusicUtilities.tgcallsrun import ASS_ACC


async def LOG_CHAT(message, what):
    if message.chat.username:
        chatusername = (f"@{message.chat.username}")
    else:
        chatusername = ("Private Group")
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")" 
    logger_text = f"""
__**Baru Hasil Pencarian**__

**Obrolan:** {message.chat.title} [`{message.chat.id}`]
**Pengguna:** {mention}
**Username:** @{message.from_user.username}
**ID Pengguna:** `{message.from_user.id}`
**Link Obrolan:** {chatusername}
**Pencarian:** {message.text}"""
    await ASS_ACC.send_message(LOG_GROUP_ID, f"{logger_text}", disable_web_page_preview=True)
    
