from telebot import TeleBot
from bot_token import TOKEN
from telebot.types import Message
from state import StateHelp
from list_alphas import list_alphas
from re import sub, findall
from telebot.custom_filters import StateFilter


bot = TeleBot(token=TOKEN)
dic = dict()


@bot.message_handler(commands=['start'])
def start(message: Message):
    russia = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    dic[message.from_user.id] = [russia, russia, russia, russia, russia, '', '']
    bot.set_state(user_id=message.from_user.id,
                  state=StateHelp.not_alpha,
                  chat_id=message.chat.id)
    print(dic)
    bot.send_message(message.from_user.id, 'Введи буквы которых точно нет: ')


@bot.message_handler(state=StateHelp.not_alpha)
def not_alpha(message: Message):
    if message.text.isalpha():
        dic[message.from_user.id][5] = message.text
    bot.set_state(user_id=message.from_user.id,
                  state=StateHelp.alpha1,
                  chat_id=message.chat.id)
    print(dic)
    bot.send_message(message.from_user.id, 'первая буква(- нет информации, а + эта буква на своем месте):')


@bot.message_handler(state=StateHelp.alpha1)
def alp1(message: Message):
    not_alp = message.text
    not_alpha = dic[message.from_user.id][0]
    if not_alp != '-' and message.text[0] == '+':
        print('True')
        dic[message.from_user.id][0] = not_alp[1]
    elif not_alp.isalpha():
        print('False')
        for e in message.text:
            dic[message.from_user.id][6] += f'(?=\w*{e})'
    print(not_alp, not_alpha)
    if not_alpha != '' and not_alp.isalpha():
        print(1)
        dic[message.from_user.id][0] = sub(fr"[{not_alpha + not_alp}]", "", dic[message.from_user.id][0])
    elif not_alpha != '':
        print(2)
        dic[message.from_user.id][0] = sub(fr"[{not_alpha}]", "", dic[message.from_user.id][0])
    elif not_alp.isalpha():
        print(3)
        dic[message.from_user.id][0] = sub(fr"[{not_alp}]", "", dic[message.from_user.id][0])

    bot.set_state(user_id=message.from_user.id,
                  state=StateHelp.alpha2,
                  chat_id=message.chat.id)
    print(dic)
    bot.send_message(message.from_user.id, 'вторая буква(- нет информации, а + эта буква на своем месте):')


@bot.message_handler(state=StateHelp.alpha2)
def alp1(message: Message):
    not_alp = message.text
    not_alpha = dic[message.from_user.id][1]

    if not_alp != '-' and message.text[0] == '+':
        dic[message.from_user.id][0] = not_alp[1]
    elif not_alp.isalpha():
        for e in message.text:
            dic[message.from_user.id][6] += f'(?=\w*{e})'

    if not_alpha != '' or not_alp.isalpha():
        dic[message.from_user.id][1] = sub(fr"[{not_alpha + not_alp}]", "", dic[message.from_user.id][1])
    elif not_alpha != '':
        dic[message.from_user.id][1] = sub(fr"[{not_alpha}]", "", dic[message.from_user.id][1])
    elif not_alp.isalpha():
        dic[message.from_user.id][1] = sub(fr"[{not_alp}]", "", dic[message.from_user.id][1])

    bot.set_state(user_id=message.from_user.id,
                  state=StateHelp.alpha3,
                  chat_id=message.chat.id)
    print(dic)
    bot.send_message(message.from_user.id, 'третья буква(- нет информации, а + эта буква на своем месте):')


@bot.message_handler(state=StateHelp.alpha3)
def alp1(message: Message):
    not_alp = message.text
    not_alpha = dic[message.from_user.id][2]
    if not_alp != '-' and message.text[0] == '+':
        dic[message.from_user.id][0] = not_alp[1]
    elif not_alp.isalpha():
        for e in message.text:
            dic[message.from_user.id][6] += f'(?=\w*{e})'

    if not_alpha != '' or not_alp.isalpha():
        dic[message.from_user.id][2] = sub(fr"[{not_alpha + not_alp}]", "", dic[message.from_user.id][2])
    elif not_alpha != '':
        dic[message.from_user.id][2] = sub(fr"[{not_alpha}]", "", dic[message.from_user.id][2])
    elif not_alp.isalpha():
        dic[message.from_user.id][2] = sub(fr"[{not_alp}]", "", dic[message.from_user.id][2])

    bot.set_state(user_id=message.from_user.id,
                  state=StateHelp.alpha4,
                  chat_id=message.chat.id)
    print(dic)
    bot.send_message(message.from_user.id, 'четвертая буква(- нет информации, а + эта буква на своем месте):')


@bot.message_handler(state=StateHelp.alpha4)
def alp1(message: Message):
    not_alp = message.text
    not_alpha = dic[message.from_user.id][3]
    if not_alp != '-' and message.text[0] == '+':
        dic[message.from_user.id][0] = not_alp[1]
    elif not_alp.isalpha():
        for e in message.text:
            dic[message.from_user.id][6] += f'(?=\w*{e})'

    if not_alpha != '' or not_alp.isalpha():
        dic[message.from_user.id][3] = sub(fr"[{not_alpha + not_alp}]", "", dic[message.from_user.id][3])
    elif not_alpha != '':
        dic[message.from_user.id][3] = sub(fr"[{not_alpha}]", "", dic[message.from_user.id][3])
    elif not_alp.isalpha():
        dic[message.from_user.id][3] = sub(fr"[{not_alp}]", "", dic[message.from_user.id][3])

    bot.set_state(user_id=message.from_user.id,
                  state=StateHelp.alpha5,
                  chat_id=message.chat.id)
    print(dic)
    bot.send_message(message.from_user.id, 'пятая буква(- нет информации, а + эта буква на своем месте):')


@bot.message_handler(state=StateHelp.alpha5)
def alp1(message: Message):
    not_alp = message.text
    not_alpha = dic[message.from_user.id][4]
    if not_alp != '-' and message.text[0] == '+':
        dic[message.from_user.id][0] = not_alp[1]
    elif not_alp.isalpha():
        for e in message.text:
            dic[message.from_user.id][6] += f'(?=\w*{e})'

    if not_alpha != '' or not_alp.isalpha():
        dic[message.from_user.id][4] = sub(fr"[{not_alpha + not_alp}]", "", dic[message.from_user.id][4])
    elif not_alpha != '':
        dic[message.from_user.id][4] = sub(fr"[{not_alpha}]", "", dic[message.from_user.id][4])
    elif not_alp.isalpha():
        dic[message.from_user.id][4] = sub(fr"[{not_alp}]", "", dic[message.from_user.id][4])
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
    print(dic)
    # alphas = findall(fr'\b{pattern}\b', list_alphas())
    # alphas = ', '.join(alphas)
    # bot.set_state(user_id=message.from_user.id,
    #               state="",
    #               chat_id=message.chat.id)
    # bot.send_message(message.from_user.id, alphas[:100])
    # bot.send_message(message.from_user.id, dic_user[6])
    bot.send_message(message.from_user.id, 'dic_user[0].__str__()')
    # bot.send_message(message.from_user.id, dic_user[1])
    # bot.send_message(message.from_user.id, dic_user[2])
    # bot.send_message(message.from_user.id, dic_user[3])
    # bot.send_message(message.from_user.id, dic_user[4])


if __name__ == '__main__':
    bot.add_custom_filter(StateFilter(bot))
    bot.infinity_polling()
