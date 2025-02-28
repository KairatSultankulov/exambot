from aiogram import types, Dispatcher


async def info_handler(message: types.Message):
    text = ("Этот бот позволяет управлять товарами и принимать заказы. "
            "Через бота клиенты могут оформлять заказы, а сотрудники могут добавлять новые товары")
    await message.answer(text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(info_handler, commands=["info"])
