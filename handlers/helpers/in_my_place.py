from .helpers_handlers import tuple_state, dic, create_user
from telebot.types import Message
from keyboards.reply import choice, back_or_menu
from loader import bot
from main import logger


@bot.message_handler(
    func=lambda message: bot.get_state(
        user_id=message.chat.id, chat_id=message.chat.id) in tuple_state and message.text == 'На своем месте'
)
def in_my_place(message: Message):
    if dic[message.from_user.id] is None:
        create_user(message.from_user.id)
        logger.debug(f'Добавлен польватель {message.from_user.id} {dic[message.from_user.id]}')

    state = bot.get_state(user_id=message.chat.id, chat_id=message.chat.id)
    bot.set_state(user_id=message.from_user.id,
                  state=state + 'in_my_place',
                  chat_id=message.chat.id)
    logger.debug(f'Установлено состояние {state + "in_my_place"} для {message.from_user.id}')
    bot.send_message(chat_id=message.from_user.id, text='Введи букву которая на своем месте:',
                     reply_markup=back_or_menu())


@bot.message_handler(
    func=lambda message: bot.get_state(
        user_id=message.chat.id, chat_id=message.chat.id).endswith('in_my_place')
)
def in_my_place(message: Message):
    if message.text.isalpha() and len(message.text) == 1:
        state = bot.get_state(user_id=message.chat.id, chat_id=message.chat.id)
        if state == tuple_state[0] + 'in_my_place':
            dic[message.from_user.id][0] = message.text.lower()
        elif state == tuple_state[1] + 'in_my_place':
            dic[message.from_user.id][1] = message.text.lower()
        elif state == tuple_state[2] + 'in_my_place':
            dic[message.from_user.id][2] = message.text.lower()
        elif state == tuple_state[3] + 'in_my_place':
            dic[message.from_user.id][3] = message.text.lower()
        elif state == tuple_state[4] + 'in_my_place':
            dic[message.from_user.id][4] = message.text.lower()
        bot.set_state(user_id=message.from_user.id,
                      state=None,
                      chat_id=message.chat.id)
        bot.send_message(chat_id=message.from_user.id, text='Готово', reply_markup=choice())
    else:
        bot.send_message(chat_id=message.from_user.id, text='Должна быть только одна буква')

