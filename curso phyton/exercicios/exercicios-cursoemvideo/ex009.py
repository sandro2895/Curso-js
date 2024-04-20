tab1 = int(input('Digite um número para ver sua tabuada : '))
cor = {'nada': '\033[m',
       'azul': '\033[36m',
       'verde': '\033[32m',
       }

print('{}={}'.format(cor['azul'], cor['nada'])*15)
print('{}{:3} x 1 = {}{}'.format(cor['verde'], tab1, tab1*1, cor['nada']))
print('{}{:3} x 2 = {}{}'.format(cor['verde'], tab1, tab1*2, cor['nada']))
print('{}{:3} x 3 = {}{}'.format(cor['verde'], tab1, tab1*3, cor['nada']))
print('{}{:3} x 4 = {}{}'.format(cor['verde'], tab1, tab1*4, cor['nada']))
print('{}{:3} x 5 = {}{}'.format(cor['verde'], tab1, tab1*5, cor['nada']))
print('{}{:3} x 6 = {}{}'.format(cor['verde'], tab1, tab1*6, cor['nada']))
print('{}{:3} x 7 = {}{}'.format(cor['verde'], tab1, tab1*7, cor['nada']))
print('{}{:3} x 8 = {}{}'.format(cor['verde'], tab1, tab1*8, cor['nada']))
print('{}{:3} x 9 = {}{}'.format(cor['verde'], tab1, tab1*9, cor['nada']))
print('{}{:3} x 10 = {}{}'.format(cor['verde'], tab1, tab1*10, cor['nada']))
print('{}='.format(cor['azul'], cor['nada'])*15)
