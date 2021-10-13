from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**𝐇𝐞𝐲 𝐈 𝐀𝐦 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 [𝐂𝐅𝐂-𝐁𝐎𝐓𝐒](https://t.me/CFC_BOT_SUPPORT
        𝐌𝐚𝐤𝐞 𝐘𝐨𝐮𝐫 𝐎𝐰𝐧 𝐁𝐨𝐭 [𝐒𝐎𝐔𝐑𝐂𝐄](https://github.com/BAZIGARX/BAZIGARMUSIC)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦🍬", url="https://github.com/BAZIGARX/BAZIGARMUSIC")
                  ],[ 
                    InlineKeyboardButton(
                        "𝗔𝗗𝗗 𝗠𝗘 𝗜𝗡 𝗚𝗥𝗢𝗨𝗣🍭", url="https://t.me/NOINOIMUSICBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝐍𝐨𝐢 𝐍𝐨𝐢 𝐈𝐬 𝐖𝐨𝐫𝐤𝐢𝐧𝐠🍭**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐎𝐰𝐧𝐞𝐫✨", url="https://t.me/BAZIGARYT")
                ]
            ]
        )
   )


