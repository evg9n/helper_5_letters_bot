from telebot import TeleBot
from bot_token import TOKEN
from telebot.storage import StateMemoryStorage

storage = StateMemoryStorage()
bot = TeleBot(token=TOKEN, state_storage=storage)
