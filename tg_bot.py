import telebot
# получение токена бота из BotFather
TOKEN = '6004830698:AAFlQT2D0UM9q7eLo-nofFU-zjebZhDFAk0'

# создание экземпляра бота
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_polling(none_stop=True,interval=0)