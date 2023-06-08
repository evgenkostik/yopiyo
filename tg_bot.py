import telebot
# получение токена бота из BotFather
TOKEN = '6004830698:AAFlQT2D0UM9q7eLo-nofFU-zjebZhDFAk0'

# создание экземпляра бота
bot = telebot.TeleBot(TOKEN)
#срабатывает по комманде /start
@bot.message_handler(commands=['start'])
#функция приветствия
def start_message(message):
#выводим сообщение приветствия
  bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler()
def answer(message):
  kd = ['как дела', 'Как дела', 'как дела?', 'Как дела?']
  if message.text in kd:
    answers = ['Всё хорошо!', 'Нормально', 'Шикарно']
    bot.send_message(message.chat.id, random.choice(answers))

if __name__ == '__main__':
  #запуск бота
#   а вас не смущает что под условием ничего нет?!
#   bot.infinity_polling находится вне условия!!!
bot.infinity_polling(none_stop=True,interval=0)
#комит Егора
#коммит жени
