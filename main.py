import wikipedia
import bot
import logging

from aiogram import Bot, Dispatcher, executor, types

wikipedia.set_lang('ru')


def search_page(name):
    """Метод для поиска нужной страницы на wiki"""
    tru_obj = wikipedia.page(name)
    return tru_obj.url


logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def welcome(message: types.Message):
    find_page = search_page(message.text)
    await message.answer(find_page)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
