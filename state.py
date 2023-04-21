from telebot.handler_backends import State, StatesGroup


class StateHelp(StatesGroup):
    not_alpha = State()
    alpha1 = State()
    alpha2 = State()
    alpha3 = State()
    alpha4 = State()
    alpha5 = State()
    result = State()
