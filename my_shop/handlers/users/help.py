from loader import dp
from aiogram import types

from aiogram.dispatcher.filters.builtin import CommandHelp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam"
            "/settings - Tilni o'zgartitish")

    await message.answer("\n".join(text))
