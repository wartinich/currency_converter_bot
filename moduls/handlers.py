from start import dp, bot, types
from moduls.keyboard import * 

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Здраствуйте!", reply_markup=main)


@dp.message_handler()
async def handler_keyboard(message: types.Message):
    if message.text == "🤖Курс криптовалюти":
        await message.answer('Bitcoin')
    elif message.text == "💰Курс доллара":
        await message.answer('Dollar')
    elif message.text == "▶Далее":
        await message.answer('Далее' ,reply_markup=menu)
    elif message.text == '💼Кошелек':
        await message.answer('Balance')
    elif message.text == '📊Статистика':
        await message.answer('Balance')
    elif message.text == '◀Назад':
        await message.answer('Назад', reply_markup=main)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


