from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
🌠𝙏𝙃𝙄𝙎 𝙄𝙎 𝙈𝘼𝘿𝙀 𝘽𝙔 𝘼𝙉𝙆𝙄𝙏 𝙁𝙊𝙍 𝙋𝙇𝘼𝙔 𝙎𝙊𝙉𝙂 \n🌺𝗥𝘂𝗻 𝗢𝗻 𝙍𝙖𝙞𝙡𝙬𝙖𝙮\n🌼𝗙𝗲𝗲𝗹 𝗛𝗶𝗴𝗵 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝗠𝘂𝘀𝗶𝗰 𝗜𝗻 𝗩𝗖 \n⭐𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 [𝘼𝙉𝙆𝙄𝙏](https://t.me/UNSTOPPABLE_ANKIT)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰𝗢𝘄𝗻𝗲𝗿❱", url="https://t.me/XD_DIE")
                  ],[
                    InlineKeyboardButton(
                        "❰𝗦𝘂𝗽𝗽𝗼𝗿𝘁❱", url="https://t.me/CHATINGADDA"
                    ),
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽❱", url="https://t.me/CHATINGADDA"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "𝗗𝗠 𝗙𝗢𝗥 𝗦𝗢𝗨𝗥𝗦𝗘", url="https://t.me/XD_DIE"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲 𝗡𝗼𝘄\n� 𝗔𝗡𝗞𝗜𝗧 𝗢𝗣 <3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌼𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/CHATINGADDA")
                ]
            ]
        )
   )
