import logging
from loader import dp

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.langKeyboard import langMenu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    text: str = f"""Salom, {message.from_user.full_name}!
Kerakli tilni tanlash!
"""
    await message.answer(text, reply_markup=langMenu)


@dp.message_handler(commands="language")
async def bot_lang(message: types.Message):
    text: str = """Tilni o'zgaritish!
Change language!"""
    await message.answer(text, reply_markup=langMenu)
