import datetime

import requests


async def get_weather():
    code_to_emoji = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q=Ufa&appid=d7d94cd3ac0212c52fc2f6af7569d737&units=metric'
    )
    weather_data = r.json()

    city = weather_data["name"]
    cur_weather = weather_data["main"]["temp"]

    weather_description = weather_data["weather"][0]["main"]
    if weather_description in code_to_emoji:
        wd = code_to_emoji[weather_description]
    else:
        wd = "Посмотри в окно, я хз че это"

    feels_weather = weather_data["main"]["feels_like"]
    wind = weather_data["wind"]["speed"]

    text = (f"***{datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}***\n"
            f"Погода в городе: {city}\n"
            f"Температура: {cur_weather}°C {wd}\n"
            f"По ощущениям: {feels_weather}°C\n"
            f"Скорость ветра: {wind} м/с")

    return text