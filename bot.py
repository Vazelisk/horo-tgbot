import telebot
import horo_getter
from flask import Flask, request
from telebot import types
import os

TOKEN = os.environ["TOKEN"]
server = Flask(__name__)

bot = telebot.TeleBot(TOKEN)

d = horo_getter.final()
keyboardmain = types.InlineKeyboardMarkup(row_width=3)
first_button = types.InlineKeyboardButton(text="Овен", callback_data="first")
second_button = types.InlineKeyboardButton(text="Телец", callback_data="second")
third_button = types.InlineKeyboardButton(text="Близнецы", callback_data="third")
fourth_button = types.InlineKeyboardButton(text="Рак", callback_data="fourth")
fifth_button = types.InlineKeyboardButton(text="Лев", callback_data="fifth")
sixth_button = types.InlineKeyboardButton(text="Дева", callback_data="sixth")
seventh_button = types.InlineKeyboardButton(text="Весы", callback_data="seventh")
eigth_button = types.InlineKeyboardButton(text="Скорпион", callback_data="eigth")
ninth_button = types.InlineKeyboardButton(text="Стрелец", callback_data="ninth")
tenth_button = types.InlineKeyboardButton(text="Козерог", callback_data="tenth")
eleventh_button = types.InlineKeyboardButton(text="Водолей", callback_data="eleventh")
twelvth_button = types.InlineKeyboardButton(text="Рыбы", callback_data="twelvth")
keyboardmain.add(first_button, second_button, third_button, fourth_button, fifth_button,
                 sixth_button, seventh_button, eigth_button, ninth_button, tenth_button,
                 eleventh_button, twelvth_button)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! Это бот, который покажет вам актуальный гороскоп",
                     reply_markup=keyboardmain)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "mainmenu":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы вернулись в меню", reply_markup=keyboardmain)

    elif call.data == "first":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=d['aries'], reply_markup=keyboard)

    elif call.data == "second":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=d['taurus'], reply_markup=keyboard)

    elif call.data == "third":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=d['gemini'], reply_markup=keyboard)

    elif call.data == "fourth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=d['cancer'], reply_markup=keyboard)

    elif call.data == "fifth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=d['leo'], reply_markup=keyboard)

    elif call.data == "sixth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=d['virgo'], reply_markup=keyboard)

    elif call.data == "seventh":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=d['libra'], reply_markup=keyboard)

    elif call.data == "eigth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=d['scorpio'], reply_markup=keyboard)

    elif call.data == "ninth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=d['sagittarius'], reply_markup=keyboard)

    elif call.data == "tenth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=d['capricorn'], reply_markup=keyboard)

    elif call.data == "eleventh":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=d['aquarius'], reply_markup=keyboard)

    elif call.data == "twelvth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=d['pisces'], reply_markup=keyboard)


# этот обработчик реагирует на любое сообщение
@bot.message_handler(func=lambda m: True)
def send_len(message):
    bot.send_message(message.chat.id, 'Напишите /start, чтобы выбрать знак зодиака')


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://horo-bot.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
