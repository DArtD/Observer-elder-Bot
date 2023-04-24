from filters.AdminMessage import AdminMessage
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from filters.IsPrivate import IsPrivate
from loader import dp


@dp.message_handler(Command('get_list'), IsPrivate())
async def get_list(message: types.Message):
    gr_list = InputFile('group_list.png')
    await dp.bot.send_photo(chat_id=message.chat.id, photo=gr_list)
