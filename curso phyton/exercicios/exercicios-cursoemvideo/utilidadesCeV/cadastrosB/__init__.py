def leiaInt(num):
    while True:
        try:
            msg = int(input(num))
        except(ValueError, TypeError):
            print('\33[31mNúmero INTEIRO invalido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário interrompeu o programa!')
            return 3
        else:
            return msg

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())

def menu(lista):
    cabecalho('\033[33mMENU PRINCIPAL\033[m')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont += 1
    print(linha())
    op = leiaInt('\033[32mDigite sua opção: \033[m')
    return op

