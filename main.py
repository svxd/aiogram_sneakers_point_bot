from aiogram import Bot, Dispatcher, executor, types
from app import keyboards as kb
from app import database as db
from dotenv import load_dotenv
import os

load_dotenv()
# Токен бота скрыт!!
bot = Bot(os.getenv('TOKEN'))

# Инициализация бота
dp = Dispatcher(bot=bot)


# Запуск database.py
async def on_startup(_):
    await db.db_start()
    print('Бот успешно запущен!')


# Приветствие
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await db.cmd_start_db(message.from_user.id)
    await message.answer_sticker('CAACAgIAAxkBAAPQZBX7EgAB7S9CaYio99Qwqn0xH7KfAALYDwACSPJgSxX7xNp4dGuYLwQ')
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в наш магазин кроссовок!',
                         reply_markup=kb.main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=kb.main_admin)


@dp.message_handler(commands=['id'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.id}')


# Кнопка: Каталог
@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer(f'Каталог пуст!', reply_markup=kb.catalog_list)


# Кнопка: Корзина
@dp.message_handler(text='Корзина')
async def cart(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAIBAAFkFf0QaoWKz3HKuXDFI8HrOmaDCgAC8wADVp29Cmob68TH-pb-LwQ')
    await message.answer(f'Корзина пуста!')


# Кнопка: Контакты
@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
    await message.answer(f'Покупать товар у него: @EgaShS')


# Кнопка: Админ-панель
@dp.message_handler(text='Админ-панель')
async def contacts(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы вошли в админ-панель', reply_markup=kb.admin_panel)
    else:
        await message.reply('Я тебя не понимаю.')


# Фильтр сообщений: Стикеры
# @dp.message_handler(content_types=['sticker'])
# async def check_sticker(message: types.Message):
#     await message.answer(message.sticker.file_id)
#     await bot.send_message(message.from_user.id, message.chat.id)

# # Фильтр сообщений: Документ, фото
# @dp.message_handler(content_types=['document', 'photo'])
# async def forward_message(message: types.Message):
#     await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)


# Пользователь пишет чушь!
@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю :(')

# callback data
@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == 't-shirt':
        await bot.send_message(chat_id=callback_query.from_user.id, text='Вы выбрали футболки')
    elif callback_query.data == 'shorts':
        await bot.send_message(chat_id=callback_query.from_user.id, text='Вы выбрали шорты')
    elif callback_query.data == 'sneakers':
        await bot.send_message(chat_id=callback_query.from_user.id, text='Вы выбрали кроссовки')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
