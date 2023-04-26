from telebot.types import Message
from keyboards.reply import menu, choice_button, back_or_menu_button
from loader import bot
from handlers.helpers.helpers_handlers import dic


@bot.message_handler(func=lambda message: message.text == choice_button[1] or message == back_or_menu_button[1])
def close(message: Message):
    if dic.get(message.from_user.id):
        dic.pop(message.from_user.id)
    bot.set_state(user_id=message.from_user.id,
                  state=None,
                  chat_id=message.chat.id)
    bot.send_message(message.from_user.id, 'Главное меню', reply_markup=menu())
