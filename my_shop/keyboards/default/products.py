from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

menuProductsUz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⌚️ Soatlar"),
            KeyboardButton(text="🎧 Quloqchinlar"),
           
        ],
        [
            KeyboardButton(text="🚖 Buyurtma berish"),
            KeyboardButton(text="🛒 Savat"),
        ],
        [
            KeyboardButton(text="🔙 Orqaga"),
            KeyboardButton(text="🏠 Bosh menyu")
        ],
    ],
    resize_keyboard=True
)

menuProductsEng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⌚️ Watches"),
            KeyboardButton(text="🎧 Headphones"),
        ],
        [
            KeyboardButton(text="🚖 Place an order"),
            KeyboardButton(text="🛒 Cart"),
        ],
        [
            KeyboardButton(text="🔙 Back"),
            KeyboardButton(text="🏠 Main menu")
        ],
    ],
    resize_keyboard=True
)

menuWathcesUz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Klassik soatlar"),
            KeyboardButton(text="Zamonaviy soatlar"),
        ],
        [
           KeyboardButton(text="🔙 Orqaga"),
           KeyboardButton(text="🏠 Bosh menyu"),
        ],
    ],
    resize_keyboard=True
)


menuWathcesEng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Classic watches"),
            KeyboardButton(text="Modern watches"),
        ],
        [
           KeyboardButton(text="🔙 Back"),
           KeyboardButton(text="🏠 Main menu"),
        ],
    ],
    resize_keyboard=True
)

menuHeadphonesUz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎧 Simli quloqchinlar"),
            KeyboardButton(text="🎧 Simsiz quloqchinlar"),
        ],
        [
            KeyboardButton(text="🔙 Orqaga"),
            KeyboardButton(text="🏠 Bosh menyu"),
        ],
    ],
    resize_keyboard=True
)


menuHeadphonesEng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎧 Wired headphones"),
            KeyboardButton(text="🎧 Wireless headphones"),
        ],
        [
            KeyboardButton(text="🔙 Back"),
            KeyboardButton(text="🏠 Main menu"),
        ],
    ],
    resize_keyboard=True
)
