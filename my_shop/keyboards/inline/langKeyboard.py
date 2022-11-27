from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

langMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Uzbek 🇺🇿", callback_data="uzbek"),
            InlineKeyboardButton(text="English 🇬🇧", callback_data="english"),
        ],
    ],
)
