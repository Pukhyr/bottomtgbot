import datetime
import random

import telebot
from telebot import types

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

def get_welcome() -> str:
    current_time = datetime.datetime.now()
    if 0<= current_time.hour <6:
        return 'Доброй ночи!'
    if 6<= current_time.hour <12:
        return 'Доброе утро!'
    if 12<= current_time.hour <18:
        return 'Добрый день!'
    else:
        return 'Добрый вечер!'


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Романтика")
    btn2 = types.KeyboardButton("Комедия")
    btn3 = types.KeyboardButton("Триллер")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text=f'{get_welcome()} Я бот, который поможет тебе выбрать, что посмотреть сегодня) Выбери жанр:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_Film(message):
    if(message.text == "Романтика"):
        with open('roman.txt', 'r', encoding='Utf-8') as file:
            romans = file.read().split('\n')
        roman = random.choice(romans)
        bot.send_message(message.chat.id, text=f'Сегодня вечером стоит посмотреть: "{roman}"')
    elif (message.text == "Комедия"):
        with open('comedy.txt', 'r', encoding='Utf-8') as file:
            cs = file.read().split('\n')
        comedy = random.choice(cs)
        bot.send_message(message.chat.id, text=f'Сегодня вечером стоит посмотреть: "{comedy}"')
    elif (message.text == "Триллер"):
        with open('threl.txt', 'r', encoding='Utf-8') as file:
            ths = file.read().split('\n')
        threl = random.choice(ths)
        bot.send_message(message.chat.id, text=f'Сегодня вечером стоит посмотреть: "{threl}"')
bot.polling(none_stop=True)



@bot.message_handler(func=lambda _: True)
def unknown_command(message: telebot.types.Message):
    bot.send_message(message.chat.id, text=f'Неизвестная команда')


if __name__=='__main__':
    print ('Бот запущен')
    bot.infinity_polling()