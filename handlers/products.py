from aiogram import types, Dispatcher
from config import database


async def show_products(message: types.Message):
    products = database.get_products()

    if not products:
        await message.answer("Товары пока не добавлены!")
        return

    for product in products:
        name, category, size, price, product_id, photo = product
        text = (f"{name}\n"
                f"Категория: {category}\n"
                f"Размер: {size}\n"
                f"Цена: {price} руб.\n"
                f"Артикул: {product_id}")

        if photo:
            await message.answer_photo(photo=photo, caption=text)
        else:
            await message.answer(text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(show_products, commands=["products"])
