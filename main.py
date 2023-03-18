from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()
# Токен бота скрыт!!
bot = Bot(os.getenv('TOKEN'))

# Инициализация бота
dp = Dispatcher(bot=bot)

# Клавиатура пользователя
main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Корзина').add('Контакты')

# Клавиатура админа
main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Контакты').add('Админ-панель')

# Админ-панель
admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Контакты').add('Сделать рассылку')


catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton(text='Футболки', url='https://vk.com/rox1xd'),
                 InlineKeyboardButton(text='Шорты', url='https://vk.com/rox1xd'),
                 InlineKeyboardButton(text='Кроссовки', url='https://vk.com/rox1xd'))


# Приветствие
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAPQZBX7EgAB7S9CaYio99Qwqn0xH7KfAALYDwACSPJgSxX7xNp4dGuYLwQ')
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в наш магазин кроссовок!',
                         reply_markup=main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=main_admin)


@dp.message_handler(commands=['id'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.id}')


# Кнопка: Каталог
@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer(f'Каталог пуст!', reply_markup=catalog_list)


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
        await message.answer(f'Вы вошли в админ-панель', reply_markup=admin_panel)
    else:
        await message.reply('Я тебя не понимаю.')

# Фильтр сообщений: Стикеры
# @dp.message_handler(content_types=['sticker'])
# async def check_sticker(message: types.Message):
#     await message.answer(message.sticker.file_id)
#     await bot.send_message(message.from_user.id, message.chat.id)
#
#
# # Фильтр сообщений: Документ, фото
# @dp.message_handler(content_types=['document', 'photo'])
# async def forward_message(message: types.Message):
#     await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)


# Пользователь пишет чушь!
@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю :(')


if __name__ == '__main__':
    executor.start_polling(dp)
