import telebot
from telebot import types
import json
import random

with open('token', 'r') as secret:
    token = secret.read()
bot = telebot.TeleBot(token)


with open('questions.json', 'r') as questions:
    questions_list = json.load(questions)['questions']


def random_question():
    try:
        number = random.randint(0, len(questions_list)-1)
        return questions_list.pop(number)
    except Exception:
        print("Кажется, вопросы кончились...")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Следующая ➡️")
    btn2 = types.KeyboardButton("Кринж 🌚")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет! Я карточный бот. Я как карточки твинби, только всратее. Чтобы начать, нажми кнопку \"Следующая\"".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Следующая ➡️":
        try:
            bot.send_message(message.from_user.id, random_question())
        except Exception:
            bot.send_message(message.from_user.id, "Кажется, вопросы кончились...")
    elif message.text == "Кринж 🌚":
        bot.send_message(message.from_user.id, "А че вы хотели, эти карточки ИИ писал...")
    else:
        pass


bot.polling(none_stop=True, interval=0)
