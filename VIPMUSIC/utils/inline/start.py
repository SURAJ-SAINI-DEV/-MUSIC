from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐇𝙴𝙻𝙿 ۞", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="✡ 𝐆𝚁𝙾𝚄𝙿 ✡", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚𝐀𝐃𝐃 𝐌𝐄 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𝐁𝐀𝐁𝐘✚",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="🦋ɢʀᴏᴜᴘ🦋", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="💠ᴄʜᴀɴɴᴇʟ💠", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text=" 🤦‍♂️ʜᴇʟᴘ🤦‍♂️ ", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                        "✌ʏᴏᴜᴛᴜʙᴇ✌", url=f"https://www.youtube.com/@allexamgkgspractice"),
            InlineKeyboardButton(
                        " 😍ᴄᴜᴛᴇ ᴏᴡɴᴇʀ😍 ", url=f"https://t.me/suraj_saini93")
        ],
    ]
    return buttons
