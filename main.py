import logging
from aiogram import executor
from config import dp, database, ADMINS, bot
from handlers import info, orders, products, start, store_fsm


async def on_startup(_):
    database.create_tables()
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text="Бот включен!")


async def on_shutdown(_):
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text="Бот выключен!")


start.register_handlers(dp)
info.register_handlers(dp)
products.register_handlers(dp)
orders.register_handlers(dp)
store_fsm.register_handlers(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
