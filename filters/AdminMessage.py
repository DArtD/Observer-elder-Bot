from data.config import admin
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class AdminMessage(BoundFilter):

    async def check(self, message: types.Message):
        return str(message.from_user.id) == admin
