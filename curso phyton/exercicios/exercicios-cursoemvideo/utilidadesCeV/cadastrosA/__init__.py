def titulo(t):
    tit = '-' * len(t)
    titu = '-' * 10
    print(f'[{titu}{tit}{titu}]')
    print(f'           {t}')
    print(f'[{titu}{tit}{titu}]')


def cadstr():

    titulo('MENU PRINCIPAL')
    print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[34mCadastrar nova Pessoa\033[m')
    print('\033[33m3\033[m - \033[34mSair do sistema\033[m')
    while True:
        try:
            nume = int(input(f'\033[32mDigite Sua opção\033[m '))

        except(TypeError, ValueError):
            print('\033[31mDigite um número inteiro valido!\033[m')
        except KeyboardInterrupt:
            return '\033[31mUsuário interrompeu a digitação\033[m'
        else:
            return f'\033[36mo numero digitado foi: {nume}\033[m '

