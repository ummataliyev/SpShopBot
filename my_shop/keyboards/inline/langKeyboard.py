from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

langMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Uzbek πΊπΏ", callback_data="uzbek"),
            InlineKeyboardButton(text="English π¬π§", callback_data="english"),
        ],
    ],
)
