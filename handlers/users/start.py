from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.IsPrivate import IsPrivate
from loader import dp


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    # start_buttons = ["Расписание на неделю", "Расписание на сегодня", "Расписание на след. учебн. день"]
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*start_buttons)
    await message.answer(f'Привет, {message.from_user.full_name}!')  #, reply_markup=keyboard)
