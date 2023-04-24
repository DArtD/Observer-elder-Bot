from aiogram import types

from data.config import admin
from loader import dp


@dp.message_handler(text="doc", content_types=types.ContentTypes.DOCUMENT)
async def bot_doc(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        await dp.bot.forward_message(chat_id=admin, from_chat_id=message.chat.id, message_id=message.message_id)
        await message.reply(text='Отправлено @Easy_Hunt')
