from aiogram import Bot, Dispatcher, executor, types
from moduls.config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    from moduls.handlers import dp
    print('Бот запущен!!!')
    executor.start_polling(dp)