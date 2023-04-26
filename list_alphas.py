import os
def list_alphas():
    print(os.path.abspath('utils/letters.txt'))
    with open('utils/letters.txt', 'r', encoding='utf-8') as f:
        alphas = f.read()
    return alphas
