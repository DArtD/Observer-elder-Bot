from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from filters.AdminMessage import AdminMessage


class IsPrivate(BoundFilter):

    async def check(self, message: types.Message):
        if await AdminMessage.check(self, message):
            return True
        else:
            return message.chat.type == types.ChatType.PRIVATE
