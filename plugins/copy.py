import os
import time

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

from pyrogram.errors import FloodWait
from pyrogram import Client, filters


@Client.on_message(filters.media)
async def forward(bot, update):
    try:
        await bot.copy_message(
            chat_id=Config.CHANNEL_ID,
            from_chat_id=update.chat.id,
            message_id=update.message_id
        )
    except FloodWait as e:
        time.sleep(e.x)
