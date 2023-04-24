import datetime
import json
from aiogram import Bot
from data.config import admin
from utils.Upper_Lower_week import UpperLowerweek


async def timetable_next(bot: Bot):
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

        return await bot.send_message(chat_id=admin, text="<b><u>Расписание на завтра</u></b>"),\
               await bot.send_message(chat_id=admin, text=await UpperLowerweek(), disable_notification=True), \
               await bot.send_message(chat_id=admin, text=timetable, disable_notification=True)
