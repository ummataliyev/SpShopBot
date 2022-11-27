from aiogram import types
from loader import dp, bot
from data.config import CHAT_ID
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import mainMenuUz, mainMenuEng
from keyboards.inline.menuWathces import classicwatches, modernwatches
from keyboards.inline.menuHeadphones import wrdheadphonesUz, wrlheadphonesUz


@dp.message_handler(Text(equals=['Klassik soatlar']))
async def show_uzclassic(message: Message):
    text: str = "Yoqtirgan soatingizni tanlang ⬇️"
    await message.answer(text, reply_markup=mainMenuUz)
    await bot.send_message(text="Sotuvdagi klassik soatlar ⬇️", chat_id=CHAT_ID, reply_markup=classicwatches)


@dp.message_handler(Text(equals=['Classic watches']))
async def show_engclassic(message: Message):
    text: str = "Choose your favorite watch ⬇️"
    await message.answer(text, reply_markup=mainMenuEng)
    await bot.send_message(text="Classic watches on sale ⬇️", chat_id=CHAT_ID, reply_markup=classicwatches)

@dp.message_handler(Text(equals=['Zamonaviy soatlar']))
async def show_uzmodern(message: Message):
    text: str = "Yoqtirgan soatingizni tanlang ⬇️"
    await message.answer(text, reply_markup=mainMenuUz)
    await bot.send_message(text="Sotuvdagi zamonaviy soatlar ⬇️", chat_id=CHAT_ID, reply_markup=modernwatches)


@dp.message_handler(Text(equals=["Modern watches"]))
async def show_engmodern(message: Message):
    text: str = "Choose your favorite watch ⬇️"
    await message.answer(text, reply_markup=mainMenuEng)
    await bot.send_message(text="Modern watches on sale ⬇️", chat_id=CHAT_ID, reply_markup=modernwatches)


@dp.message_handler(Text(equals=["🎧 Simli quloqchinlar"]))
async def wrd_earphonesuz(message: Message):
    text: str = "Yoqtirgan quloqchiningizni tanlang ⬇️"
    await message.answer(text, reply_markup=mainMenuUz)
    await bot.send_message(text="Sotuvdagi simli quloqchinarl ⬇️", chat_id=CHAT_ID, reply_markup=wrdheadphonesUz)


@dp.message_handler(Text(equals=["🎧 Wired headphones"]))
async def wrd_earphoneseng(message: Message):
    text: str = "Choose your favorite headphones ⬇️"
    await message.answer(text, reply_markup=mainMenuEng)
    await bot.send_message(text="Wired headphones for sale ⬇️", chat_id=CHAT_ID, reply_markup=wrdheadphonesUz)


@dp.message_handler(Text(equals=["🎧 Simsiz quloqchinlar"]))
async def wrl_headphones(message: Message):
    text: str = "Yoqtirgan quloqchiningizni tanlang ⬇️"
    await message.answer(text, reply_markup=mainMenuUz)
    await bot.send_message(text="Sotuvdagu simsiz quloqchinlar ⬇️", chat_id=CHAT_ID, reply_markup=wrlheadphonesUz)


@dp.message_handler(Text(equals=["🎧 Wireless headphones"]))
async def wrd_earphoneseng(message: Message):
    text: str = "Choose your favorite headphones ⬇️"
    await message.answer(text, reply_markup=mainMenuEng)
    await bot.send_message(text="Wired headphones for sale ⬇️", chat_id=CHAT_ID, reply_markup=wrlheadphonesUz)
