def snotas(p=0, t=0, d=0):
    total = t * p / 100
    div = total / d
    print(f'menos \033[32m{p}%\033[m porcento de \033[34m{t}\033[m = \033[31m{total:.2f}\033[m')
    print(f'\033[33m{d}\033[m dividindo \033[34m{total}\033[m = \033[31m{div}\033[m ')
    print('-=-' * 20)


print(' prod 1'), snotas(60, 850, 10)

