import telebot
from telebot import apihelper
from telebot import types
import urllib
import config

f = open('out1.jpg','wb')
f.write(urllib.request.urlopen(config.TIMETABLE1).read())
f.close()

f = open('out2.jpg','wb')
f.write(urllib.request.urlopen(config.TIMETABLE2).read())
f.close()

f = open('out3.jpg','wb')
f.write(urllib.request.urlopen(config.TIMETABLE3).read())
f.close()

bot = telebot.TeleBot(config.TOKEN)
#apihelper.proxy = {'https':config.PROXY}

@bot.message_handler(commands = ["start"])
def start(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_timetable = types.KeyboardButton(text="Расписание")
    button_timetable_all = types.KeyboardButton(text="Всё pаcпиcаниe")
    button_cloud = types.KeyboardButton(text="Облако")
    button_prepods = types.KeyboardButton(text="Преподы")
    keyboard.add(button_timetable, button_timetable_all,button_cloud,button_prepods)
    bot.send_message(message.chat.id, "Обновление", reply_markup=keyboard)

@bot.message_handler(regexp="Облако")
def handle_message(message):
    bot.send_message(message.chat.id, 'https://yadi.sk/d/xHYI54zrJfTXLA')

@bot.message_handler(regexp="Расписание")
def send_photo(message):
    bot.send_chat_action(message.chat.id, 'upload_photo')
    img1 = open('out1.jpg', 'rb')
    bot.send_photo(message.chat.id, img1)

@bot.message_handler(regexp="Преподы")
def send_photo(message):
    bot.send_message(message.chat.id, config.PREPODS)

@bot.message_handler(regexp="Всё pаcпиcаниe")
def send_all(message):
    	#bot.send_chat_action(message.chat.id, 'upload_photo')
	    img1 = open('out1.jpg', 'rb')
	    img2 = open('out2.jpg', 'rb')
	    img3 = open('out3.jpg', 'rb')
	    bot.send_photo(message.chat.id, img1)
	    bot.send_photo(message.chat.id, img2)
	    bot.send_photo(message.chat.id, img3)

@bot.message_handler(content_types=['document', 'audio', 'video','photo'])
def handle_docs_audio(message):
	bot.send_message(message.chat.id, 'Что это такое?')

@bot.message_handler(func=lambda message: True)
def send_all(message):
	pass

# Запуск
bot.polling(none_stop=True)

