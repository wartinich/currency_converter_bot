from moduls.config import TOKEN
from moduls.scraper import *
import telebot



bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, f'Здраствуйте!\nКурс криптовалют - /crypto_rate\nКурс валют - /money_rate ')


@bot.message_handler(commands=['crypto_rate'])
def send_welcome(message):
	bot.send_message(message.chat.id, crypto_rating)

if __name__ == "__main__":
    print('The bot is running!')
    bot.polling()
