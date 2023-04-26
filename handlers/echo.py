from telebot.types import Message
from loader import bot


@bot.message_handler(content_types=['text', 'sticker', 'audio'])
def bot_echo(message: Message):
    bot.send_message(chat_id=message.chat.id, text='Че?')
