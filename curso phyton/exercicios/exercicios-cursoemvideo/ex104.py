def leaInt(n):
    cores = {'branco': '\33[m',
             'red': '\033[31m'}
    n = str(input('Digite um número: ')).strip()
    while not n.isnumeric():
        print(f'{cores["red"]}ERRO! Digite um número inteiro válido.{cores["branco"]}')
        n = str(input('Digite um número: ')).strip()
    return n


# Programa principal:
num = leaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
