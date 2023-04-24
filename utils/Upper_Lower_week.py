import datetime


async def UpperLowerweek():
    timedelta = datetime.datetime.now() - datetime.datetime(2023, 2, 6)

    if int(timedelta.days / 7) % 2 == 0:
        text = ("<b>Верхняя неделя</b>")

    else:
        text = ("<b>Нижняя неделя</b>")

    return text
