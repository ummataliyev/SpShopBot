from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


cb = CallbackData('buy', 'id', 'name')

classicwatches = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Cartier", callback_data='buy:0:Cartier'),
            InlineKeyboardButton(text="Vecheron", callback_data='buy:1:watchVecheron'),
        ],
        [
            InlineKeyboardButton(text="Patek Philippe", callback_data='buy:2:watchPP'),
            InlineKeyboardButton(text="Rolex", callback_data='buy:3:watchRolex:'),
        ],
        [
            InlineKeyboardButton(text="Zenith", callback_data='buy:4:watchZenith:'),
            InlineKeyboardButton(text="TAG Heuer", callback_data='buy:5:watchheuer'),
        ],
    ],
)

modernwatches = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="iWatch", callback_data='buy:6:wIwatch:$800'),
            InlineKeyboardButton(text="G-Shock", callback_data='buy:7:wGshock:$$414'),
        ],
        [
            InlineKeyboardButton(text="Richar Mille", callback_data='buy:8:wRM:$267447'),
            InlineKeyboardButton(text="Audemars Piguet", callback_data='buy:9:wAP:$288847'),
        ],
    ],
)



#watchCartier = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton("Buy"),
#         ],
#     ],
# )

# watchVecheron = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton("Buy", url=watchVecheron),
#         ],
#     ],
# )

# watchPP = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton("Buy", url=watchVecheron),
#         ],
#     ],
# )

# watchRolex = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton("Buy", url=watchVecheron),
#         ],
#     ],
# )

# watchZenith = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton("Buy", url=watchVecheron),
#         ],
#     ],
# )

# watchHeuer = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton("Buy", url=watchVecheron),
#         ],
#     ],
# )

