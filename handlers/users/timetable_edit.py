import json
from pprint import pprint

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.types import InputFile

from filters.AdminMessage import AdminMessage
from loader import dp
from states import TimetableEdit


@dp.message_handler(Command("timetable_edit"), AdminMessage())
async def edit_start(message: types.Message):
    edit_req = InputFile('edit_req.png')
    await message.answer("Функция изменения расписания\n"
                         "Пожалуйста, придерживайтесь рекомендованной форме заполнения расписания"
                         "\nРекомендации к заполнению:")
    await dp.bot.send_photo(chat_id=message.chat.id, photo=edit_req)
    await message.answer("Какой день недели хотите изменить? (0 = пн, 4 = пт):")

    await TimetableEdit.Q1.set()


@dp.message_handler(state=TimetableEdit.Q1)
async def pair_choice(message: types.Message, state: FSMContext):
    answer = message.text
    with open("timetable.json", encoding="UTF-8") as f:
        obj = f.read()
        obj1 = json.loads(obj)

        await message.answer(obj1[answer])
        await message.answer("Какую пару хотите изменить? (first_pair - fourth_pair):")

        await TimetableEdit.Q1.set()


@dp.message_handler(state=TimetableEdit.Q2)
async def pair_edit(message: types.Message):
    with open("timetable.json", 'w') as f:
        pass




