import telebot
from telebot import types

bot = telebot.TeleBot('5312347011:AAHX1Hlf26XDk3B8dfFziBYnRn_gORXIE0E')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите называние направления')


@bot.message_handler()
def NumbersGroups(message):
    if message.text.strip().lower() == 'ист':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button1 = types.KeyboardButton('ИСТ-20-1б')
        button2 = types.KeyboardButton('ИСТ-20-2б')
        button3 = types.KeyboardButton('ИСТ-20-3б')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'Выбирете группу', reply_markup=markup)

    if message.text == 'ИСТ-20-1б':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button1 = types.KeyboardButton('Предметы')
        button2 = types.KeyboardButton('Преподаватели')
        button3 = types.KeyboardButton('Расписание')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=markup)
    elif message.text == 'ИСТ-20-2б':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button1 = types.KeyboardButton('Предметы')
        button2 = types.KeyboardButton('Преподаватели')
        button3 = types.KeyboardButton('Расписание')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=markup)
    elif message.text == 'ИСТ-20-3б':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button1 = types.KeyboardButton('Предметы')
        button2 = types.KeyboardButton('Преподаватели')
        button3 = types.KeyboardButton('Расписание')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=markup)

    getMessage = message.text.strip().lower()
    if getMessage == 'предметы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        button1 = types.KeyboardButton('УИР')
        button2 = types.KeyboardButton('ТИПиС')
        button3 = types.KeyboardButton('ЯП')
        button4 = types.KeyboardButton('ТП')
        button5 = types.KeyboardButton('Физкультура')
        button6 = types.KeyboardButton('ВМ')
        button7 = types.KeyboardButton('ТИ')
        markup.add(button1, button2, button3, button4, button5, button6, button7)
        bot.send_message(message.chat.id, "Выбирете предмет", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button1 = types.KeyboardButton('Предметы')
        button2 = types.KeyboardButton('Преподаватели')
        button3 = types.KeyboardButton('Расписание')
        markup.add(button1, button2, button3)
    # else:
    #   bot.send_message(message.chat.id, 'Такого направления нет в базе данных')


@bot.message_handler(content_types=['text'])
def GroupElemets(message):
    getMessage = message.text.strip().lower()
    if getMessage == 'предметы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        button1 = types.KeyboardButton('УИР')
        button2 = types.KeyboardButton('ТИПиС')
        button3 = types.KeyboardButton('ЯП')
        button4 = types.KeyboardButton('ТП')
        button5 = types.KeyboardButton('Физкультура')
        button6 = types.KeyboardButton('ВМ')
        button7 = types.KeyboardButton('ТИ')
        markup.add(button1, button2, button3, button4, button5, button6, button7)
        finalMessage = "Выбирете предмет"
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button1 = types.KeyboardButton('Предметы')
        button2 = types.KeyboardButton('Преподаватели')
        button3 = types.KeyboardButton('Расписание')
        markup.add(button1, button2, button3)
        finalMessage = "Такого предмета не существует"
    bot.send_message(message.chat.id, finalMessage, reply_markup=markup)


bot.polling(none_stop=True)
