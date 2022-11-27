from data import config
from aiogram import Bot, Dispatcher, types
# from utils.db_api.postgresql import Database
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# db = Database()