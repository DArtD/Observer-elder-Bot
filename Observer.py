import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loader import bot
from utils.timetable_next_cron import timetable_next
from utils.set_bot_commands import set_default_commands
from utils.timetable_today_cron import timetable_today_cron


async def on_startup(dp):
    import filters
    import middlewares

    filters.setup(dp)
    middlewares.setup(dp)

    scheduler_today = AsyncIOScheduler(timezone="Asia/Yekaterinburg")
    scheduler_today.add_job(timetable_today_cron, trigger='cron', hour=7, minute=0,
                            start_date=datetime.datetime.now(), kwargs={'bot': bot})

    scheduler_next = AsyncIOScheduler(timezone="Asia/Yekaterinburg")
    scheduler_next.add_job(timetable_next, trigger='cron', hour=19, minute=0,
                           start_date=datetime.datetime.now(), kwargs={'bot': bot})

    scheduler_today.start()
    scheduler_next.start()

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)


async def on_shutdown(dp):
    from utils.notify_admins import on_shutdown_notify
    await on_shutdown_notify(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
