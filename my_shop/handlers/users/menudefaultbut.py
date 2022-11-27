from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.products import menuHeadphonesUz, menuHeadphonesEng
from keyboards.default.menuKeyboard import menuUz, menuEng, info_Uz, info_Eng
from keyboards.default.products import menuProductsUz, menuProductsEng, menuWathcesUz, menuWathcesEng

@dp.message_handler(text='🔥 Mahsulotlar')
async def show_uzproduct(message: Message):
    text: str = "Kerakli bo'limni tanlang:"
    await message.answer(text, reply_markup=menuProductsUz)


@dp.message_handler(text="ℹ️ Ma'lumot")
async def info_uz(message: Message):
    text: str = "Kerakli bo'limni tanlang  ⬇️"
    await message.answer(text, reply_markup=info_Uz)


@dp.message_handler(text='ℹ️ Information')
async def info_eng(message: Message):
    text: str = "Select the desired section ⬇️"
    await message.answer(text, reply_markup=info_Eng)


@dp.message_handler(text="🔥 Products")
async def show_engproduct(message: Message):
    text: str = "Select the desired section ⬇️"
    await message.answer(text, reply_markup=menuProductsEng)


@dp.message_handler(text='🏠 Bosh menyu')
async def back_uzmain(message: Message):
    text: str = "Select the desired section ⬇️"
    await message.answer(text, reply_markup=menuUz)


@dp.message_handler(text='🏠 Main menu')
async def back_engmain(message: Message):
    text: str = "Select the desired section ⬇️"
    await message.answer(text, reply_markup=menuEng)

@dp.message_handler(text='⌚️ Soatlar')
async def show_uzwatch(message: Message):
    text: str = "Qanday turdagi soatlar sizni qiziqtiradi?"
    await message.answer(text, reply_markup=menuWathcesUz)


@dp.message_handler(text='⌚️ Watches')
async def show_engwatch(message: Message):
    text: str = "What kind of watches are you interested in?"
    await message.answer(text, reply_markup=menuWathcesEng)


@dp.message_handler(text='🎧 Quloqchinlar')
async def show_uzearphones(message: Message):
    text: str = "Qanday turdagi quloqchinlar sizni qiziqtiradi?"
    await message.answer(text, reply_markup=menuHeadphonesUz)


@dp.message_handler(text="🎧 Headphones")
async def show_engearphones(message: Message):
    text: str = "What kind of headphones are you interested in?"
    await message.answer(text, reply_markup=menuHeadphonesEng)


# @dp.message_handler(text="")




# # @dp.callback_query_handler(text_contains='Cartier')
# # async def cartier(call: CallbackQuery):
# #     await call.answer(cache_time=60)
# #     await call.message.answer("Buy it", reply_markup=watchCartier)
