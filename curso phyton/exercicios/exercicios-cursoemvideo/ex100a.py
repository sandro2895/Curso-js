import random


def sorteia(num):
    cont = 0
    while True:
        num.append(random.randint(1, 10))
        cont += 1
        if cont == 5:
            break
    print(f'Números sorteados:', end=' ')
    for cont in num:
        if cont % 2 == 0:
            print(f'[+ {cont} +]', end=' ')
        else:
            print(f'[> {cont} <]', end=' ')
    print()
def somaPar(spar):
    soma = 0
    for cont in spar:
        if cont % 2 == 0:
            soma += cont
    print(f'Soma de todos os números pares: [= {soma} =]')



numeros = []
sorteia(numeros)
somaPar(numeros)
