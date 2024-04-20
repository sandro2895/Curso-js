num1 = int(input('Digite um número : '))
cor = {'nada': '\033[m',
       'amarelo': '\033[4:33m',
       'azul': '\033[4:36m'}
print('O número digitado foi : \033[4m{}\033[m'.format(num1))
print('-O sucessor de \033[4m{}\033[m é : {}{}{}'.format(num1, cor['azul'], num1 + 1, cor['nada']))
print('-O antecessor de \033[4m{}\033[m é : {}{}{}'.format(num1, cor['amarelo'], num1 - 1, cor['nada']))
