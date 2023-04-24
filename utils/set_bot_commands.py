from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("about_me", "Обо мне"),
        types.BotCommand("weather", "Погода в Уфе(для разработки)"),
        types.BotCommand("timetable", " Актуальное расписание"),
        types.BotCommand("timetable_today", "Расписание на сегодня"),
        types.BotCommand("timetable_next", "Расписание на след. учебный день"),
        types.BotCommand("get_list", "Список группы"),
        types.BotCommand("get_list_tx", "Список группы в сообщении")
    ])
