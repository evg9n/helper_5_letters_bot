from telebot.types import Message
from keyboards.reply import menu
from loader import bot


@bot.message_handler(commands=['start'])
def commands_start(message: Message):
    bot.send_message(message.from_user.id, 'Привет', reply_markup=menu())
