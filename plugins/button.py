# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1, FORCE_SUB_GROUP, FORCE_SUB_GROUP2, FORCE_SUB_CHANNEL2
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟸", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟹", url=client.invitelink2),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟺", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟻", url=client.invitelink6),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟼", url=client.invitelink5),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟸", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟹", url=client.invitelink2),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟺", url=client.invitelink3),
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟻", url=client.invitelink6),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟼", url=client.invitelink5),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
