from loader import dp
from aiogram import executor

import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # await db.create()
    # #await db.drop_users()
    # await db.create_table_users()
    # await db.create_table_products()

   # Default commands (/start and /help)
    await set_default_commands(dispatcher)
    
    #Notifies the admin that the bot has started
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
