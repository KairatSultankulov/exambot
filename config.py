from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import dotenv_values
from database import Database

config = dotenv_values(".env")
BOT_TOKEN = config["BOT_TOKEN"]

ADMINS = [359455298]

STAFF = [359455298, ]

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
database = Database("database.sqlite3")
