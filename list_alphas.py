def list_alphas():
    with open('+.txt', 'r', encoding='utf-8') as f:
        alphas = f.read()
    return alphas