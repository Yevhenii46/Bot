import telebot
from telebot import types

bot = telebot.TeleBot('5518249124:AAHxGw0NN4IkWndPbDXn9IB5xYaEGClnjqQ')

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Djinni', url='https://djinni.co/')
    btn2 = types.InlineKeyboardButton('DOU', url='https://jobs.dou.ua/')
    btn3 = types.InlineKeyboardButton('Rabota.ua', url='https://rabota.ua/ua/zapros/junior-qa-engineer/')
    btn4 = types.InlineKeyboardButton('Work.ua', url='https://www.work.ua/ru/jobs-kyiv-junior+qa/')

    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Hello, {0.first_name} ! For search some vacancies please select a resource.'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    bot.send_message(message.chat.id, "Please, select a resource",parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Wow, nice photo!")

@bot.message_handler(content_types=['audio'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Hmm, I dont understand :(")

bot.polling(none_stop=True)