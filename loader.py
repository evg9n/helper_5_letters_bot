from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from os import environ
from dotenv import load_dotenv

load_dotenv()
TOKEN = environ.get('TOKEN')

storage = StateMemoryStorage()

bot = TeleBot(token=TOKEN, state_storage=storage)
