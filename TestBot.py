import telebot
from telebot import types
import config
import datetime
import json

date = datetime.date.weekday(datetime.date.today())
bot = telebot.TeleBot(config.token)
chain_actions = []
with open('departments.json') as f1:
    departments_json = json.load(f1)
with open('groups.json') as f2:
    groups_json = json.load(f2)
with open('teachers.json') as f3:
    teachers_json = json.load(f3)

list_of_teachers = []
[[[list_of_teachers.append([k, teachers_json['faculties'][j][i][k]]) for k in teachers_json['faculties'][j][i]] for i in teachers_json['faculties'][j]]
 for j in teachers_json['faculties']]


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "Приветствую вас!\nЗачем пожаловали?")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    markup.add('Факультеты', 'Преподаватели')
    bot.send_message(message.chat.id, "Выбирай, дядя", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def start_text(message):
    if message.text == 'Факультеты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in departments_json['faculties']:
            markup.add(i)
        bot.send_message(message.chat.id, "Выберите факультет", reply_markup=markup)
        bot.register_next_step_handler(message, g)
    elif message.text == 'Преподаватели':
        bot.send_message(message.chat.id, "Введите фамилию преподавателя")
        bot.register_next_step_handler(message, p)


def p(message):
    teachers = []
    reply_markup = types.InlineKeyboardMarkup(row_width=2)
    for i in list_of_teachers:
        if i[0].split(' ')[0] == message.text:
            teachers.append(i)
    for i in teachers:
        reply_markup.add(types.InlineKeyboardButton(text=i[0], url=i[1]))
    bot.send_message(message.chat.id, "Держи, дядя", reply_markup=reply_markup)


def g(message):
    if message.text in list(departments_json['faculties'].keys()):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for direction in groups_json['faculties'][replace(message.text)].keys():
            markup.add(direction)
        chain_actions.append(replace(message.text))
        bot.send_message(message.chat.id, "Выберите направление", reply_markup=markup)
        bot.register_next_step_handler(message, a)


def a(message):
    if message.text in list(groups_json['faculties'][chain_actions[-1]].keys()):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in groups_json['faculties'][chain_actions[-1]][message.text].keys():
            markup.add(i)
        chain_actions.append(message.text)
        bot.send_message(message.chat.id, "Выберите группу", reply_markup=markup)
        bot.register_next_step_handler(message, b)


def b(message):
    if message.text in list(groups_json['faculties'][chain_actions[-2]][chain_actions[-1]].keys()):
        reply_markup = types.InlineKeyboardMarkup(row_width=2)
        for i in groups_json['faculties'][chain_actions[-2]][chain_actions[-1]][message.text].keys():
            url = groups_json['faculties'][chain_actions[-2]][chain_actions[-1]][message.text][i]
            reply_markup.add(types.InlineKeyboardButton(text=i, url=url))
        chain_actions.append(message.text)
        bot.send_message(message.chat.id, "Качай", reply_markup=reply_markup)


# факультет/направление/специальность/конкретная специальность
def replace(word):
    abb = {'AKF': 'АКФ',
           'GNF': 'ГНФ',
           'GUM': 'ГумФ',
           'MTF': 'МТФ',
           'STF': 'СФ',
           'FPMM': 'ФПММ',
           'HTF': 'ХТФ',
           'ETF': 'ЭТФ',
           }
    return abb[word]


bot.polling(none_stop=True)
