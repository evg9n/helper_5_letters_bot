from os.path import abspath, join
from loader import constants


def list_alphas():
    with open(abspath(join('dictionaries', constants.CURRENT_LETTERS)), 'r', encoding='utf-8') as f:
        alphas = f.read()
    return alphas
