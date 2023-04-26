from telebot.types import ReplyKeyboardMarkup, KeyboardButton


menu_button = ('Начать',)
choice_button = ('Показать', 'Отмена', 'Уточнить каких букв точно нет',
                 '1 буква', '2 буква', '3 буква', '4 буква', '5 буква', 'Сбросить')
back_or_menu_button = ('Назад', 'Главное меню')
alpha_button = ('На своем месте', "Не на своем месте")


def choice() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button = [
        KeyboardButton(text=choice_button[0]),
        KeyboardButton(text=choice_button[1]),
        KeyboardButton(text=choice_button[2]),
        KeyboardButton(text=choice_button[3]),
        KeyboardButton(text=choice_button[4]),
        KeyboardButton(text=choice_button[5]),
        KeyboardButton(text=choice_button[6]),
        KeyboardButton(text=choice_button[7]),
        KeyboardButton(text=choice_button[8])
    ]

    return markup.add(*button)


def clos() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(KeyboardButton('Отмена'))


def menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(KeyboardButton(text=menu_button[0]))


def back_or_menu() -> ReplyKeyboardMarkup:
    button = [
        KeyboardButton(back_or_menu_button[0]),
        KeyboardButton(back_or_menu_button[1])
    ]
    return ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(*button)


def alpha() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = [KeyboardButton(text=alpha_button[0]),
              KeyboardButton(text=alpha_button[1]),
              KeyboardButton(text=back_or_menu_button[0]),
              KeyboardButton(text=back_or_menu_button[1])
              ]
    return markup.add(*button)


if __name__ == "__main__":
    print('Показать' in choice_button)
