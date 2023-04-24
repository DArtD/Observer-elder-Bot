from aiogram import types

from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        await message.answer(message.text)
