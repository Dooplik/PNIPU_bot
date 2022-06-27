import telebot
from telebot import types
import config
import parse
import datetime
from config import step as s

bot = telebot.TeleBot(config.token)
chain_actions = []


@bot.message_handler(commands=["start"])
def welcome(message):
    chain_actions.clear()
    bot.send_message(message.chat.id,
                     "Приветствую вас, пока что я уродец и работаю только для истов 20 года, но скоро это изменится!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    b1 = types.KeyboardButton('ИСТ-20-1б')
    b2 = types.KeyboardButton('ИСТ-20-2б')
    b3 = types.KeyboardButton('ИСТ-20-3б')
    markup.add(b1, b2, b3)
    bot.send_message(message.chat.id,
                     "Я знаю, что твоё направление ИСТ, так что просто выбери группу",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def start_text(message):
    if message.text in ['ИСТ-20-1б', 'ИСТ-20-2б', 'ИСТ-20-3б']:
        chain_actions.append(message.text)
        print(chain_actions)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        b1 = types.KeyboardButton('Предметы')
        b2 = types.KeyboardButton('Преподаватели')
        b3 = types.KeyboardButton('Расписание')
        b4 = types.KeyboardButton('Назад')
        markup.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=markup)
    elif message.text in ['Расписание', 'расписание']:
        if 'ИСТ-20-1б' in chain_actions:
            print(1)
            chain_actions.append(message.text)
            rasp = parse.parse(config.path1)
            bot.send_message(message.chat.id, rasp)
        elif 'ИСТ-20-2б' in chain_actions:
            print(2)
            chain_actions.append(message.text)
            rasp = parse.parse(config.path2)
            bot.send_message(message.chat.id, rasp)
        elif 'ИСТ-20-3б' in chain_actions:
            print(3)
            chain_actions.append(message.text)
            rasp = parse.parse(config.path3)
            bot.send_message(message.chat.id, rasp)
    elif message.text == "Назад":
        welcome(message)


bot.polling(none_stop=True)
