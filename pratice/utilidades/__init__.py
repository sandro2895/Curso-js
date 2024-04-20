def arquivexist(ex):
    try:
        a = open(ex, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arquivcriar(ex):
    try:
        a = open(ex, 'wt+')
        print('Arquivo criado com sucesso!')
    except FileNotFoundError:
        return False
    else:
        return True

def arquivabrir(ex):
    try:
        a = open(ex, 'rt')

    except FileNotFoundError:
        print('arquivo não encontrado! ')
    else:
        print('Pessoas cadastradas')
        print(a.read())

