import telebot
from random import randint
from datetime import datetime

TOKEN = "8366644844:AAGqWNFPVqoYjdV1vYaMsrUTFxup_4QicMU"
bot = telebot.TeleBot (TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    def send_welcome (message) :
        try:
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = telebot.types.KeyboardButton(text="Игра в кубик")
            button2 = telebot.types.KeyboardButton(text="Игровой автомат")
            keyboard.add(button1, button2)
            bot.send_message(message.chat.id, "Привет,меня зовут Бот", reply_markup=keyboard)
        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка {e}" )



@bot.message_handler(commands=["date"])
def date(message):
    bot.send_message(message.chat.id, "сейчас"+ str(datetime.today()))


@bot.message_handler(commands=["random"])
def random (message):
    bot.send_message(message.chat.id, "Случайное число: " + str(randint(1, 1000 )))


@bot.message_handler(commands=["image"])
def send_image(send_message) :
    try:
       file = open("image")
       bot.send_photo(message.chat.id, file,caption="Изображение кота:")
       file.close()
except Exception as e :
bot.send_message(message.chat.id, f"Ошибка: {e}")


@bot.message_handler(content_types=["text"])
def answer(message):
    try:
        text = message.text
        if text == "Привет":
            bot.send_message(message.chat.id,"Привет")
        elif text =="Как дела":
            bot.send_message(message.chat.id, "Отлично")
        elif text == "Как тебя зовут" :
            bot.send_message(message.chat.id,"Меня зовут бот")
        elif text =="Игра в кубик":
            value = bot.send_message(message.chat.id, emoji="🎰").dice.value
            if value in (1, 16, 22, 32, 43, 48):
                bot.send_message(message.chat.id, "Победа")
            elif value == 64:
                bot.send_message(message.chat.id, "Jacpot")
            else:
                bot.send_message(message.chat.id, "Попробуй еще раз")
        elif text == "Игра в кубик":
            keyboard2 = telebot.types.ReplyKeyboardMarkup(row_width=3)
            button1 = telebot.types.InlineKeyboardButton("1", callback_data="1")
            button2 = telebot.types.InlineKeyboardButton("2", callback_data="2")
            button3 = telebot.types.InlineKeyboardButton("3", callback_data="3")
            button4 = telebot.types.InlineKeyboardButton("4", callback_data="4")
            button5 = telebot.types.InlineKeyboardButton("5", callback_data="5")
            button6 = telebot.types.InlineKeyboardButton("6", callback_data="6")
            keyboard2.add(button1, button2, button3, button4, button5,button6)
            bot.send_message(message.chat.id,"Угадай число на кубике", reply_markup=keyboard2)
        else:
            bot.send_message(message.chat.id, text)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")

@bot.callback_query_handler(func=lambda call: call.data in("1","2","3","4","5","6",))
def dice_answer(call):
    value = bot.send_dice(call.message.chat.id, emoji="").dice.value
    if str(value) == call.data:
        bot.send_message(call.message.chat.id,"Победа")
    else:
        bot.send_message(call.message.chat.id,"Попробуй еще раз")


bot.polling(none_stop=True, interval=0)
