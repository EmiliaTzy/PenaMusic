from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaDocument,
    InputMediaVideo,
    InputMediaAudio,
    Message,
)
from Zaid import app
from pyrogram import Client, filters
from youtubesearchpython import VideosSearch
import lyricsgenius
import re

@Client.on_callback_query(filters.regex(pattern=r"lyrics"))
async def lyricssex(_,CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    try:
        id, user_id = callback_request.split("|") 
    except Exception as e:
        return await CallbackQuery.message.edit(f"❌ Error Occured\n✅ **Possible reason could be**:{e}")
    url = (f"https://www.youtube.com/watch?v={id}")
    print(url)
    try:
        results = VideosSearch(url, limit=1)
        for result in results.result()["result"]:
            title = (result["title"])
    except Exception as e:
        return await CallbackQuery.answer("❌ Sound not found, Youtube issues...", show_alert=True)   
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    print(title)
    t = re.sub(r'[^\w]', ' ', title)
    print(t)
    y.verbose = False
    S = y.search_song(t, get_full_info=False)
    if S is None:
        return await CallbackQuery.answer("❌ Lirik Tidak Ditemukan hehehe", show_alert=True)
    await CallbackQuery.message.delete()
    userid = CallbackQuery.from_user.id
    usr = f"[{CallbackQuery.from_user.first_name}](tg://user?id={userid})"
    xxx = f"""
**Pencarian Lirik Diatur Oleh Eiko Music Player**

**Pencarian Oleh:-** {usr}
**Pencarian Lagu:-** __{title}__

**Lirik Ditemukan Untuk:-** __{S.title}__
**Artis:-** {S.artist}

**__Lirik:__**

{S.lyrics}"""
    await CallbackQuery.message.reply_text(xxx)
    
    
@Client.on_message(filters.command("lyrics"))
async def lrsearch(_, message: Message):  
    m = await message.reply_text("🔎 Mencari Lirik")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("❌ Lirik tidak ditemukan hehehe")
    xxx = f"""
**Pencarian Lirik Diatur Oleh Eiko Music Player**

**Pencarian Lagu:-** __{query}__

**Lirik Ditemukan Untuk:-** __{S.title}__
**Artis:-** {S.artist}

**__Lirik:__**

{S.lyrics}"""
    await m.edit(xxx)
