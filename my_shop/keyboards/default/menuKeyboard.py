from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuUz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔥 Mahsulotlar"),
            KeyboardButton(text="🛒 Savat"),
        ],
        [
            KeyboardButton(text="ℹ️ Ma'lumot"),
        ],
    ],
    resize_keyboard=True,
)

menuEng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔥 Products"),
            KeyboardButton(text="🛒 Cart"),
        ],
        [
            KeyboardButton(text="ℹ️ Information"),
        ],
    ],
    resize_keyboard=True,
)

info_Uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚀 Yetkazib berish shartlari"),
            KeyboardButton(text="☎️ Biz bilan bog'lanish uchun"),
        ],
        [
            KeyboardButton(text="🏠 Bosh menyu"),
        ],
    ],
    resize_keyboard=True,
)


info_Eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚀 Delivery conditions"),
            KeyboardButton(text="☎️ To contact us"),
        ],
        [
            KeyboardButton(text="🏠 Main menu"),
        ],
    ],
    resize_keyboard=True,
)

mainMenuUz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠 Bosh menyu")
        ],
    ],
    resize_keyboard=True
)

mainMenuEng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠 Main menu")
        ],
    ],
    resize_keyboard=True
)