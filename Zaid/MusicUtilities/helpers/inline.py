from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)

from Zaid import BOT_USERNAME
def play_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="▷", callback_data=f'resumevc2'),
                InlineKeyboardButton(text="II", callback_data=f'pausevc2'),
                InlineKeyboardButton(text="‣‣I", callback_data=f'skipvc2'),
                InlineKeyboardButton(text="▢", callback_data=f'stopvc2')
            ],
            [
                InlineKeyboardButton(text="🔎 Lirik", callback_data=f'lyrics {videoid}|{user_id}'),
                InlineKeyboardButton(text="⚙ Menu", callback_data=f'other {videoid}|{user_id}'),
            ],
            [      
                InlineKeyboardButton(text="✘", callback_data=f'close2')
            ],
        ]
    return buttons 


def others_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="➕ Playlistmu", callback_data=f'playlist {videoid}|{user_id}'),
                InlineKeyboardButton(text="➕ Grup Playlist", callback_data=f'group_playlist {videoid}|{user_id}')
            ],
            [
                InlineKeyboardButton(text="⬇️ Unduh Audio", callback_data=f'gets audio|{videoid}|{user_id}'),
                InlineKeyboardButton(text="⬇️ Unduh Video", callback_data=f'gets video|{videoid}|{user_id}')
            ],
            [
                InlineKeyboardButton(text="⬅️  Kembali", callback_data=f'goback {videoid}|{user_id}'),
                InlineKeyboardButton(text="✘", callback_data=f'close2')
            ],
        ]
    return buttons 





play_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "▷", callback_data="resumevc"
                    ),
                    InlineKeyboardButton(
                        "II", callback_data="pausevc"
                    ),
                    InlineKeyboardButton(
                        "‣‣I", callback_data="skipvc"
                    ),
                    InlineKeyboardButton(
                        "▢", callback_data="stopvc"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✘", callback_data="close"
                    )
                ]    
            ]
        )

def audio_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="▷", callback_data=f'resumevc2'),
                InlineKeyboardButton(text="II", callback_data=f'pausevc2'),
                InlineKeyboardButton(text="‣‣I", callback_data=f'skipvc2'),
                InlineKeyboardButton(text="▢", callback_data=f'stopvc2')
            ],
            [
                InlineKeyboardButton(text="✘", callback_data="close2")              
            ],
        ]
    return buttons 


def search_markup(ID1, ID2, ID3, ID4, ID5, duration1, duration2, duration3, duration4, duration5, user_id, query):
    buttons= [
            [
                InlineKeyboardButton(text="1️⃣", callback_data=f'Music2 {ID1}|{duration1}|{user_id}'),
                InlineKeyboardButton(text="2️⃣", callback_data=f'Music2 {ID2}|{duration2}|{user_id}'),
                InlineKeyboardButton(text="3️⃣", callback_data=f'Music2 {ID3}|{duration3}|{user_id}')
            ],
            [ 
                InlineKeyboardButton(text="4️⃣", callback_data=f'Music2 {ID4}|{duration4}|{user_id}'),
                InlineKeyboardButton(text="5️⃣", callback_data=f'Music2 {ID5}|{duration5}|{user_id}')
            ],
            [ 
                
                InlineKeyboardButton(text="⬅️", callback_data=f'popat 1|{query}|{user_id}'), 
                InlineKeyboardButton(text="✘", callback_data=f"ppcl2 smex|{user_id}") ,
                InlineKeyboardButton(text="➡️", callback_data=f'popat 1|{query}|{user_id}')             
            ],
        ]
    return buttons   

def search_markup2(ID6, ID7, ID8, ID9, ID10, duration6, duration7, duration8, duration9, duration10 ,user_id, query):
    buttons= [
            [
                InlineKeyboardButton(text="6️⃣", callback_data=f'Music2 {ID6}|{duration6}|{user_id}'),
                InlineKeyboardButton(text="7️⃣", callback_data=f'Music2 {ID7}|{duration7}|{user_id}'),
                InlineKeyboardButton(text="8️⃣", callback_data=f'Music2 {ID8}|{duration8}|{user_id}')
            ],
            [ 
                InlineKeyboardButton(text="9️⃣", callback_data=f'Music2 {ID9}|{duration9}|{user_id}'),
                InlineKeyboardButton(text="🔟", callback_data=f'Music2 {ID10}|{duration10}|{user_id}')
            ],
            [ 
                
                InlineKeyboardButton(text="⬅️", callback_data=f'popat 2|{query}|{user_id}'), 
                InlineKeyboardButton(text="✘", callback_data=f"ppcl2 smex|{user_id}") ,
                InlineKeyboardButton(text="➡️", callback_data=f'popat 2|{query}|{user_id}')             
            ],
        ]
    return buttons 


def personal_markup(link):
    buttons= [
            [
                InlineKeyboardButton(text="Lihat Di Youtube", url=f'{link}')
            ],
            [ 
                InlineKeyboardButton(text="✘", callback_data=f'close2')
            ],
        ]
    return buttons   
  
start_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan Ke Grupmu", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📜 Perintah", url="https://telegra.ph/𝗕ooo--‌ᴀꜰᴋ-ᴏꜰꜰʟɪɴᴇ-08-19-2"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✘", callback_data="close2"
                    )
                ]    
            ]
        )
    
confirm_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "Ya", callback_data="cbdel"
                    ),
                    InlineKeyboardButton(
                        "Tidak", callback_data="close2"
                    )
                ]    
            ]
        )

confirm_group_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "Ya", callback_data="cbgroupdel"
                    ),
                    InlineKeyboardButton(
                        "Tidak", callback_data="close2"
                    )
                ]    
            ]
        )

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "✘", callback_data="close2"
                    )
                ]    
            ]
        )

play_list_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "Playlistmu", callback_data="P_list"
                    ),
                    InlineKeyboardButton(
                        "Grup Playlist", callback_data="G_list"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✘", callback_data="close2"
                    )
                ]
            ]
        )

def playlist_markup(user_name, user_id):
    buttons= [
            [
                InlineKeyboardButton(text=f"Grup Playlist", callback_data=f'play_playlist {user_id}|group'),
            ],
            [
                InlineKeyboardButton(text=f"{user_name[:8]}'s Playlist", callback_data=f'play_playlist {user_id}|personal'),
            ],
            [
                InlineKeyboardButton(text="✘", callback_data="close2")              
            ],
        ]
    return buttons
