import telebot
from telebot import types
import datetime
import json

token = '5418188464:AAFhdYgDC3bgn-ziUyY0e4IfZ6A55eTJOXA'
date = datetime.date.weekday(datetime.date.today())
bot = telebot.TeleBot(token)

with open('departments.json') as f1:
    departments_json = json.load(f1)
with open('groups.json') as f2:
    groups_json = json.load(f2)
with open('teachers.json') as f3:
    teachers_json = json.load(f3)
with open('glossary.json') as f4:
    glossary_json = json.load(f4)

list_of_teachers = []
[[[list_of_teachers.append([k, teachers_json['faculties'][j][i][k]]) for k in teachers_json['faculties'][j][i]]
  for i in teachers_json['faculties'][j]]for j in teachers_json['faculties']]


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "Приветствую вас!\nЗачем пожаловали?")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    markup.add('Расписание', 'Преподаватели', 'Справочник')
    bot.send_message(message.chat.id, "Выбирай, дядя", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def start_text(message):
    if message.text == 'Расписание':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in departments_json['faculties']:
            markup.add(replace(i))
        bot.send_message(message.chat.id, "Выберите факультет", reply_markup=markup)
        bot.register_next_step_handler(message, find_direction)
    elif message.text == 'Преподаватели':
        bot.send_message(message.chat.id, "Введите фамилию преподавателя")
        bot.register_next_step_handler(message, find_teachers)
    elif message.text == 'Справочник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in glossary_json.keys():
            markup.add(i)
        bot.send_message(message.chat.id, "Выбери чёнить", reply_markup=markup)
        bot.register_next_step_handler(message, glossary)


def find_teachers(message):
    teachers = []
    reply_markup = types.InlineKeyboardMarkup(row_width=2)
    for i in list_of_teachers:
        if i[0].split(' ')[0] == message.text:
            teachers.append(i)
    for i in teachers:
        reply_markup.add(types.InlineKeyboardButton(text=i[0], url=i[1]))
    bot.send_message(message.chat.id, "Держи, дядя", reply_markup=reply_markup)


def find_direction(message):
    if replace(message.text) in list(departments_json['faculties'].keys()):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for direction in groups_json['faculties'][message.text].keys():
            markup.add(direction)
        faculty = message.text
        bot.send_message(message.chat.id, "Выберите направление", reply_markup=markup)
        bot.register_next_step_handler(message, find_group, faculty)


def find_group(message, faculty):
    if message.text in list(groups_json['faculties'][faculty].keys()):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in groups_json['faculties'][faculty][message.text].keys():
            markup.add(i)
        group = message.text
        bot.send_message(message.chat.id, "Выберите группу", reply_markup=markup)
        bot.register_next_step_handler(message, list_schedule, faculty, group)


def list_schedule(message, faculty, group):
    if message.text in list(groups_json['faculties'][faculty][group].keys()):
        reply_markup = types.InlineKeyboardMarkup(row_width=2)
        for i in groups_json['faculties'][faculty][group][message.text].keys():
            url = groups_json['faculties'][faculty][group][message.text][i]
            reply_markup.add(types.InlineKeyboardButton(text=i, url=url))
        bot.send_message(message.chat.id, "Качай", reply_markup=reply_markup)


def glossary(message):
    if message.text in list(glossary_json.keys()):
        reply_markup = types.InlineKeyboardMarkup(row_width=2)
        for i in glossary_json[message.text].keys():
            url = glossary_json[message.text][i]
            reply_markup.add(types.InlineKeyboardButton(text=i, url=url))
        bot.send_message(message.chat.id, "Смотри", reply_markup=reply_markup)


def replace(word):
    abb = {'AKF': 'АКФ', 'GNF': 'ГНФ', 'GUM': 'ГумФ', 'MTF': 'МТФ', 'STF': 'СФ', 'FPMM': 'ФПММ', 'HTF': 'ХТФ',
           'ETF': 'ЭТФ',
           'АКФ': 'AKF', 'ГНФ': 'GNF', 'ГумФ': 'GUM', 'МТФ': 'MTF', 'СФ': 'STF', 'ФПММ': 'FPMM', 'ХТФ': 'HTF',
           'ЭТФ': 'ETF'}
    return abb[word]


bot.polling(none_stop=True)
