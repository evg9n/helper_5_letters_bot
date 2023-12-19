from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from constants import Constants

constants = Constants()

storage = StateMemoryStorage()

bot = TeleBot(token=constants.BOT_TOKEN, state_storage=storage)
