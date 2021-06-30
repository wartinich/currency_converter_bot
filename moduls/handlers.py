from aiogram.types import base
from start import dp, bot, types
from moduls.keyboard import * 
from pycoingecko import CoinGeckoAPI
from py_currency_converter import convert
from aiogram.dispatcher.filters import Text


cg = CoinGeckoAPI()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Здраствуйте, {0.first_name}!".format(message.from_user), reply_markup=main)


#crypto rate
@dp.message_handler(Text(equals="🤖Курс криптовалюти"))
async def crypto_rate(message: types.Message):
    price = cg.get_price(ids="bitcoin,ethereum,cardano,ripple,dogecoin", vs_currencies="usd")
    await message.answer(f"📊 Bitcoin - ${price['bitcoin']['usd']}\n"
                         f"📊 Ethereum - ${price['ethereum']['usd']}\n"
                         f"📊 Cardano - ${price['cardano']['usd']}\n"
                         f"📊 XRP - ${price['ripple']['usd']}\n"
                         f"📊 Dogecoin - ${price['dogecoin']['usd']}")


#money rate
@dp.message_handler(Text(equals='💰Курс доллара'))
async def money_rate(message: types.Message):
    dollar = convert(base='USD', amount=1, to=['UAH'])
    euro = convert(base='EUR', amount=1, to=['UAH'])
    await message.answer(f"1 _$ = {dollar['UAH']} _₴\n"
                         f"1 _€ = {euro['UAH']} _₴", parse_mode='Markdown')


#keyboard hendler
@dp.message_handler()
async def handler_keyboard(message: types.Message):
    if message.text == "🤖Курс криптовалюти":
        await message.answer('Bitcoin')
    elif message.text == "💰Курс валют":
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


