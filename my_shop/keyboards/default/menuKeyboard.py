from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuUz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="đĨ Mahsulotlar"),
            KeyboardButton(text="đ Savat"),
        ],
        [
            KeyboardButton(text="âšī¸ Ma'lumot"),
        ],
    ],
    resize_keyboard=True,
)

menuEng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="đĨ Products"),
            KeyboardButton(text="đ Cart"),
        ],
        [
            KeyboardButton(text="âšī¸ Information"),
        ],
    ],
    resize_keyboard=True,
)

info_Uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="đ Yetkazib berish shartlari"),
            KeyboardButton(text="âī¸ Biz bilan bog'lanish uchun"),
        ],
        [
            KeyboardButton(text="đ  Bosh menyu"),
        ],
    ],
    resize_keyboard=True,
)


info_Eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="đ Delivery conditions"),
            KeyboardButton(text="âī¸ To contact us"),
        ],
        [
            KeyboardButton(text="đ  Main menu"),
        ],
    ],
    resize_keyboard=True,
)

mainMenuUz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="đ  Bosh menyu")
        ],
    ],
    resize_keyboard=True
)

mainMenuEng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="đ  Main menu")
        ],
    ],
    resize_keyboard=True
)