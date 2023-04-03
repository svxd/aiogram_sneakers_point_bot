from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


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