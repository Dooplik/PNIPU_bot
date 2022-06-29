import telebot
from telebot import types
import config
import parse
import datetime
import json

date = datetime.date.weekday(datetime.date.today())
bot = telebot.TeleBot(config.token)
chain_actions = []
with open('departments.json') as f:
    loaded_json = json.load(f)


def schedule(mes, d=datetime.date.weekday(datetime.date.today())):
    if 'ИСТ-20-1б' in chain_actions:
        print(1)
        chain_actions.append(mes.text)
        rasp = parse.parse_xlsx(config.path1, d)
        bot.send_message(mes.chat.id, rasp)
    elif 'ИСТ-20-2б' in chain_actions:
        print(2)
        chain_actions.append(mes.text)
        rasp = parse.parse_xlsx(config.path2, d)
        bot.send_message(mes.chat.id, rasp)
    elif 'ИСТ-20-3б' in chain_actions:
        print(3)
        chain_actions.append(mes.text)
        rasp = parse.parse_xlsx(config.path3, d)
        bot.send_message(mes.chat.id, rasp)


@bot.message_handler(commands=["start"])
def welcome(message):
    chain_actions.clear()
    bot.send_message(message.chat.id,
                     "Приветствую вас, пока что я уродец и работаю только для истов 20 года, но скоро это изменится!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in loaded_json['faculties']:
        markup.add(i)
    bot.send_message(message.chat.id,
                     "Я знаю, что твоё направление ИСТ, так что просто выбери группу",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def start_text(message):
    if message.text in list(loaded_json['faculties'].keys()):
        pass
    if message.text in ['ИСТ-20-1б', 'ИСТ-20-2б', 'ИСТ-20-3б']:
        chain_actions.append(message.text)
        print(chain_actions)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        b1 = types.KeyboardButton('Предметы')
        b2 = types.KeyboardButton('Преподаватели')
        b3 = types.KeyboardButton('Расписание')
        b4 = types.KeyboardButton('На главную')
        markup.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=markup)
    elif message.text in ['Расписание', 'расписание']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        b1 = types.KeyboardButton('На сегодня')
        b2 = types.KeyboardButton('На завтра')
        b4 = types.KeyboardButton('На главную')
        markup.add(b1, b2, b4)
        bot.send_message(message.chat.id, "На какой день смотреть будем, дядя?", reply_markup=markup)
        print(message.text)
    elif message.text == 'На сегодня':
        print(message.text)
        schedule(message)
    elif message.text == 'На завтра':
        print(message.text)
        schedule(message, date + 1)
    elif message.text == "На главную":
        welcome(message)


bot.polling(none_stop=True)
