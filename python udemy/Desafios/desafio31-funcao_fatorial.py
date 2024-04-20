from math import factorial


def fatorial(f=0):
    if f > 0:
        print(f'O fatorial de {f} é: {factorial (f)}')
    else:
        print(f'O fatorial de {f} é {factorial (f)}')


fatorial(10)
