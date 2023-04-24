import os

from dotenv import load_dotenv

load_dotenv()

group_chat = os.getenv("GROUP_CHAT")
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admin = os.getenv("ADMIN_ID")
OPEN_WEATHER_TOKEN = str(os.getenv("OPEN_WEATHER_TOKEN"))

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
