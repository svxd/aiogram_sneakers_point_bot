from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
# Токен бота скрыт!
bot = Bot(os.getenv('TOKEN'))
# Инициализация бота
dp = Dispatcher(bot=bot)


# Приветствие
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в наш магазин кроссовок!')


# Пользователь пишет чушь!
@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю :(')


if __name__ == '__main__':
    executor.start_polling(dp)