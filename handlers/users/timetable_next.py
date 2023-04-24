import datetime
import json
from aiogram.dispatcher.filters import Command
from aiogram import types

from filters.IsPrivate import IsPrivate
from loader import dp


@dp.message_handler(Command('timetable_next'), IsPrivate())
async def timetable_next(message: types.Message):
    dt_day = datetime.date.today().weekday()
    if 4 <= dt_day <= 6:
        dt_day = 0
    else:
        dt_day += 1

    timetable = ''
    with open('timetable.json', encoding="utf-8") as f:
        obj1 = f.read()
        obj = json.loads(obj1)
        for i in obj[str(dt_day)]:
            timetable += '\n' + obj[str(dt_day)][i] + '\n'
        await message.answer(timetable)
