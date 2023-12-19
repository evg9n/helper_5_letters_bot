from os import environ, path, listdir

from dotenv import load_dotenv


class Constants:

    def __init__(self):
        path_env = path.abspath('env')

        try:
            for env in listdir(path_env):
                if env.endswith('.env'):
                    load_dotenv(path.join(path_env, env))
        except FileNotFoundError:
            pass

        self.BOT_TOKEN = environ.get('BOT_TOKEN')
        self.CURRENT_LETTERS = environ.get('CURRENT_LETTERS')

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('Constants are not changeable!')
        else:
            super().__setattr__(name, value)