from aiogram import types, Dispatcher


async def info_handler(message: types.Message):
    text = ("Этот бот позволяет клиентам оформлять заказы, а сотрудники могут добавлять через него новые товары")
    await message.answer(text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(info_handler, commands=["info"])
