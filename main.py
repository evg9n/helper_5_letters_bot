from loader import bot
from telebot.custom_filters import StateFilter
import handlers
from logging import getLogger, DEBUG
from logging.config import dictConfig
from telebot.types import BotCommand
from os import path


FORMAT = "%(levelname)-8s [%(asctime)s] %(message)s"
datefmt = '%d.%m.%y %H:%M:%S'

log_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standart': {
            'format': FORMAT,
            'datefmt': datefmt
        }

    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': DEBUG,
            'formatter': 'standart',
            'stream': 'ext://sys.stdout'
        },
        'file_handler': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': DEBUG,
            'filename': path.abspath(path.join("loggers", "logger.log")),
            'encoding': 'utf-8',
            'when': 'D',
            'interval': 1,
            'backupCount': 500,
            'formatter': 'standart'
        }
    },
    'loggers': {
        '': {
            'handlers': ['file_handler', 'console'],
            'level': DEBUG
        }
    }
}

dictConfig(log_config)

logger = getLogger()


DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку")
)


if __name__ == '__main__':
    logger.debug("Запуск бота")
    bot.add_custom_filter(StateFilter(bot))
    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
    bot.infinity_polling()
