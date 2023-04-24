import os

from dotenv import load_dotenv

load_dotenv()

group_chat = "-811639370"
BOT_TOKEN = '6008950844:AAEzzRDQO12uDLN74hfMbSZDNE6qRBJ2Lbc'
admin = '1982872796'
OPEN_WEATHER_TOKEN = "d7d94cd3ac0212c52fc2f6af7569d737"

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
