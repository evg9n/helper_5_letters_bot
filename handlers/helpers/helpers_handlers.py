import random
from telebot.types import Message
from state import StateHelp
from list_alphas import list_alphas
from re import findall, sub
from keyboards.reply import choice, menu_button, choice_button, back_or_menu, back_or_menu_button, alpha, menu
from loader import bot
from main import logger


dic = dict()
tuple_state = ('StateHelp:alpha1', 'StateHelp:alpha2', 'StateHelp:alpha3',
               'StateHelp:alpha4', 'StateHelp:alpha5')


def create_user(user_id):
    russia = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    dic[user_id] = [russia, russia, russia, russia, russia, '', '']


@bot.message_handler(func=lambda message: message.text == choice_button[1] or message == back_or_menu_button[1])
def close(message: Message):
    if dic.get(message.from_user.id):
        dic.pop(message.from_user.id)
        logger.debug(f'Удален польватель {message.from_user.id}')
    bot.set_state(user_id=message.from_user.id,
                  state=None,
                  chat_id=message.chat.id)
    bot.send_message(message.from_user.id, 'Главное меню', reply_markup=menu())


@bot.message_handler(func=lambda message: message.text == menu_button[0] or message.text == choice_button[8])
def start(message: Message):
    create_user(message.from_user.id)

    if message.text == choice_button[8]:
        logger.debug(f'Сброшен польватель {message.from_user.id} {dic[message.from_user.id]}')
        bot.send_message(message.from_user.id, 'Настройки сброшены', reply_markup=choice())
    else:
        logger.debug(f'Добавлен польватель {message.from_user.id} {dic[message.from_user.id]}')
        bot.send_message(message.from_user.id, 'Выбери:', reply_markup=choice())


@bot.message_handler(
    func=lambda message:
    message.text in choice_button[2:]
    or message.text == choice_button[0]
    or message.text == back_or_menu_button[0]
)
def choice_handler(message: Message):
    if dic[message.from_user.id] is None:
        create_user(message.from_user.id)
        logger.debug(f'Добавлен польватель {message.from_user.id} {dic[message.from_user.id]}')

    if message.text == back_or_menu_button[0]:
        logger.debug(f'Назад {message.from_user.id}: {dic[message.from_user.id]}')
        bot.set_state(user_id=message.from_user.id,
                      state=None,
                      chat_id=message.chat.id)
        bot.send_message(chat_id=message.from_user.id, text='Выбирай)', reply_markup=choice())
    elif message.text == choice_button[0]:
        logger.debug(f'Показ пользователя {message.from_user.id}: {dic[message.from_user.id]}')
        dic_user = dic[message.from_user.id]
        pattern = f"{dic_user[6]}" \
                  f"[{dic_user[0]}]" \
                  "{1}" \
                  f"[{dic_user[1]}]" \
                  "{1}" \
                  f"[{dic_user[2]}]" \
                  "{1}" \
                  f"[{dic_user[3]}]" \
                  "{1}" \
                  f"[{dic_user[4]}]" \
                  "{1}"
        alphas = list_alphas()
        mes = list(set(findall(fr'\b{pattern}\b', alphas)))

        if len(mes) > 585:
            mes = [random.choice(mes) for _ in range(585)]

        if len(mes) == 0:
            logger.error(f'Слов не было найдена для {message.from_user.id} {mes}')
            bot.send_message(chat_id=message.from_user.id, text='Слов не было найдена, попробуй сбросить и заново')
        else:
            mes = ', '.join(mes)
            bot.send_message(chat_id=message.from_user.id, text=mes)

    elif message.text == choice_button[2]:
        logger.debug(f'Уточнение каких именно букв нет {message.from_user.id}: {dic[message.from_user.id]}')
        bot.set_state(user_id=message.from_user.id,
                      state=StateHelp.not_alpha,
                      chat_id=message.chat.id)
        bot.send_message(chat_id=message.from_user.id,
                         text='Пришли буквы\nПример: абвг...',
                         reply_markup=back_or_menu())
    else:
        if message.text == choice_button[3]:
            logger.debug(f'1 буква {message.from_user.id}: {dic[message.from_user.id]}')
            bot.set_state(user_id=message.from_user.id,
                          state=StateHelp.alpha1,
                          chat_id=message.chat.id)
        elif message.text == choice_button[4]:
            logger.debug(f'2 буква {message.from_user.id}: {dic[message.from_user.id]}')
            bot.set_state(user_id=message.from_user.id,
                          state=StateHelp.alpha2,
                          chat_id=message.chat.id)
        elif message.text == choice_button[5]:
            logger.debug(f'3 буква {message.from_user.id}: {dic[message.from_user.id]}')
            bot.set_state(user_id=message.from_user.id,
                          state=StateHelp.alpha3,
                          chat_id=message.chat.id)
        elif message.text == choice_button[6]:
            logger.debug(f'4 буква {message.from_user.id}: {dic[message.from_user.id]}')
            bot.set_state(user_id=message.from_user.id,
                          state=StateHelp.alpha4,
                          chat_id=message.chat.id)
        elif message.text == choice_button[7]:
            logger.debug(f'5 буква {message.from_user.id}: {dic[message.from_user.id]}')
            bot.set_state(user_id=message.from_user.id,
                          state=StateHelp.alpha5,
                          chat_id=message.chat.id)
        logger.debug(f'Активировано состояние: {bot.get_state(user_id=message.from_user.id, chat_id=message.chat.id)}')
        bot.send_message(chat_id=message.from_user.id, text='Выбери:', reply_markup=alpha())


# in_my_place
# @bot.message_handler(
#     func=lambda message: bot.get_state(
#         user_id=message.chat.id, chat_id=message.chat.id) in tuple_state and message.text == 'На своем месте'
# )
# def in_my_place(message: Message):
#     state = bot.get_state(user_id=message.chat.id, chat_id=message.chat.id)
#     bot.set_state(user_id=message.from_user.id,
#                   state=state + 'in_my_place',
#                   chat_id=message.chat.id)
#     bot.send_message(chat_id=message.from_user.id, text='Введи букву которая на своем месте:',
#                      reply_markup=back_or_menu())


# @bot.message_handler(
#     func=lambda message: bot.get_state(
#         user_id=message.chat.id, chat_id=message.chat.id) in tuple_state and message.text == 'Не на своем месте'
# )
# def in_my_not_place(message: Message):
#     state = bot.get_state(user_id=message.chat.id, chat_id=message.chat.id)
#     bot.set_state(user_id=message.from_user.id,
#                   state=state + 'in_my_not_place',
#                   chat_id=message.chat.id)
#     bot.send_message(chat_id=message.from_user.id, text='Введи букву которая не на своем месте:',
#                      reply_markup=back_or_menu())


@bot.message_handler(state=StateHelp.not_alpha)
def not_alpa_handlert(message: Message):
    if dic[message.from_user.id] is None:
        create_user(message.from_user.id)
        logger.debug(f'Добавлен польватель {message.from_user.id} {dic[message.from_user.id]}')

    if message.text.isalpha():
        delete = ''
        for a in message.text.lower():
            if a not in dic[message.from_user.id][6]:
                delete += a

        logger.debug(f'Исключение букв {delete} {message.from_user.id}: {dic[message.from_user.id]}')
        if len(dic[message.from_user.id][0]) != 1:
            dic[message.from_user.id][0] = sub(fr'[{delete}]', '', dic[message.from_user.id][0])

        if len(dic[message.from_user.id][1]) != 1:
            dic[message.from_user.id][1] = sub(fr'[{delete}]', '', dic[message.from_user.id][1])

        if len(dic[message.from_user.id][2]) != 1:
            dic[message.from_user.id][2] = sub(fr'[{delete}]', '', dic[message.from_user.id][2])

        if len(dic[message.from_user.id][3]) != 1:
            dic[message.from_user.id][3] = sub(fr'[{delete}]', '', dic[message.from_user.id][3])

        if len(dic[message.from_user.id][4]) != 1:
            dic[message.from_user.id][4] = sub(fr'[{delete}]', '', dic[message.from_user.id][4])

        bot.set_state(user_id=message.from_user.id,
                      state=None,
                      chat_id=message.chat.id)
        bot.send_message(chat_id=message.from_user.id,
                         text='Готово',
                         reply_markup=choice())
    else:
        bot.send_message(chat_id=message.from_user.id,
                         text='Только буквы хочу видеть)\nПришли пожалуйста в формате "абвг..."')
