import datetime
import json
from aiogram.dispatcher.filters import Command
from aiogram import types

from filters.IsPrivate import IsPrivate
from loader import dp


@dp.message_handler(Command('timetable_today'), IsPrivate())
async def timetable_today(message: types.Message):
    dt_day = datetime.date.today().weekday()
    if 0 <= dt_day <= 4:
        timetable = ''
        with open('timetable.json', encoding="utf-8") as f:
            obj1 = f.read()
            obj = json.loads(obj1)
            for i in obj[str(dt_day)]:
                 timetable += '\n' + obj[str(dt_day)][i] + '\n'
            await message.answer(timetable)
    else:
        await message.answer("<b>Сегодня нет пар</b>")
