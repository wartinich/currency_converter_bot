from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# one_time_keyboard=True - клавиатура пропадает после нажатия

rate = ['🤖Курс криптовалюти', '💰Курс валют', '▶Далее']
main = ReplyKeyboardMarkup(resize_keyboard=True).add(*rate)

url = ['💼Кошелек', '📊Статистика', '◀Назад']
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(*url)

