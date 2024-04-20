import math
num1 = int(input('Digite um número. '))
num2 = num1 % 2
cor = {'branco': '\033[m',
       'cinza': '\033[4:37m',
       'red': '\033[4:31m',
       'azul': '\033[4:34m'}


if num2 == 0:
    print('O número: {}{}{} é {}PAR!{}'
          .format(cor['cinza'], num1, cor['branco'], cor['red'], cor['branco']))

else:
    print('O número: {}{}{} é {}IMPAR!{}'
          .format(cor['cinza'], num1, cor['branco'], cor['azul'], cor['branco']))
