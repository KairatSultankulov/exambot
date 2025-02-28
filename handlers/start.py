from aiogram import types, Dispatcher


async def start_handler(message: types.Message):
    await message.answer("Здравтсвуйте! Это бот для управления заказами и товарами.")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
