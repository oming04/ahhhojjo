# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1, FOR_SUB_CHANNEL2, FORCE_SUB_GROUP, FORCE_SUB_GROUP1, FORCE_SUB_GROUP2
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP1 and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP and FORCE_SUB_GROUP1 and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ 1", url=client.invitelink4),
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ 2", url=client.invitelink5),
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ 3", url=client.invitelink6),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP1 and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ 1", url=client.invitelink1),
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ 2", url=client.invitelink2),
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ 3", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
     if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP and FORCE_SUB_GROUP1 and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
                InlineKeyboardButton(text="GRUP 1", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 2", url=client.invitelink2),
                InlineKeyboardButton(text="GRUP 2", url=client.invitelink5),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 3", url=client.invitelink3),
                InlineKeyboardButton(text="GRUP 3", url=client.invitelink6),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP and FORCE_SUB_GROUP1 and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ 1", url=client.invitelink4),
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ 2", url=client.invitelink5),
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ 3", url=client.invitelink6),
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
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP1 and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ 1", url=client.invitelink1),
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ 2", url=client.invitelink2),
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ 3", url=client.invitelink3),
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
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP and FORCE_SUB_GROUP1 and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
                InlineKeyboardButton(text="GRUP 1", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 2", url=client.invitelink2),
                InlineKeyboardButton(text="GRUP 2", url=client.invitelink5),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 3", url=client.invitelink3),
                InlineKeyboardButton(text="GRUP 3", url=client.invitelink6),
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
