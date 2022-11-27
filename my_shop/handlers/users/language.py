from aiogram import types
from loader import dp, bot
from keyboards.default.menuKeyboard import menuUz, menuEng


@dp.callback_query_handler(lambda c: True)
async def callback_query(call: types.CallbackQuery):
    chat_id: int = call.message.chat.id
    call_back_message = call._values.get('data')

    if call_back_message == "uzbek":
        await bot.send_message(
            chat_id=chat_id,
            text="O'zbek tili tanlandi!",
            reply_markup=menuUz
        )
        await call.answer("O'zbek tilini tanladingiz")

    if call_back_message == "english":
        await bot.send_message(
            chat_id=chat_id,
            text="English language is selected!",
            reply_markup=menuEng
        )
