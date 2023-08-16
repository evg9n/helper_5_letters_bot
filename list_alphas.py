from os.path import abspath


def list_alphas():
    with open(abspath('letters.txt'), 'r', encoding='utf-8') as f:
        alphas = f.read()
    return alphas
