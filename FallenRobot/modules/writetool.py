import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from FallenRobot import BOT_NAME, BOT_USERNAME
from FallenRobot import pbot as fallen


@fallen.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await fallen.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = f"https://api.sdbots.tk/write?text={text}"
        req = requests.get(API).url
        caption = f"""
Successfully Written Text ๐

โจ **Written By :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
๐ฅ **Requested by :** {message.from_user.mention}
โ **Link :** `{req}`
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("โข แดแดสแดษขสแดแดฉส โข", url=f"{req}")]]
            ),
        )
    else:
        lol = message.reply_to_message.text
        m = await fallen.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = f"https://api.sdbots.tk/write?text={lol}"
        req = requests.get(API).url
        caption = f"""
Successfully Written Text ๐

โจ **Written By :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
๐ฅ **Requested by :** {message.from_user.mention}
โ **Link :** `{req}`
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("โข แดแดสแดษขสแดแดฉส โข", url=f"{req}")]]
            ),
        )


__mod_name__ = "โญ๐๐๐๐๐๐"

__help__ = """

 Writes the given text on white page with a pen ๐

โ /write <text> *:* Writes the given text.
โคออออโข๐๐๐จ๐ฐ๐๐ซ๐๐ ๐๐ฒ โโ๐ [@Farooq_is_KING](https://t.me/Farooq_is_KING) โฆโอ๐ฎ๐ณ ๐ 
 """
