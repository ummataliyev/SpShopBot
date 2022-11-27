from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cb = CallbackData('buy', 'id', 'name', 'price')

wrdheadphonesUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Airpods", callback_data='buy:001:airpods:$250'),
            InlineKeyboardButton(text="Mi TWS", callback_data='buy:002:mitws:$25'),
        ],
        [
            InlineKeyboardButton(text="Tecno Hipods", callback_data='buy:003:hipods:$30'),
            InlineKeyboardButton(text="Riff on-ear", callback_data='buy:004:riff:$45')
        ],
    ],
)

wrlheadphonesUz= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="BassHeads 900", callback_data='buy:005:bassHeads:$40'),
            InlineKeyboardButton(text="Nighttinagle", callback_data='buy:006:mitws:$40'),
        ],
        [
            InlineKeyboardButton(text="Phillips SHE370BK", callback_data='buy:007:hipods:$25'),
            InlineKeyboardButton(text="Vogues", callback_data='buy:008:riff:$13')
        ],
    ],         
)
