viag = float(input('Quantos Quilômetros vai se essa viagem? '))
viag2 = viag * 0.50
viag3 = viag * 0.45
cor = {'branco': '\033[m',
       'red': '\033[31m',
       'verde': '\033[32m',
       'blue': '\033[34m'}

if viag <= 200.00:
    print('Sua viagem foi de: {}{:.2f}Km{} então o preço vai ser: {}{:.2f}R$'
          .format(cor['verde'], viag, cor['branco'], cor['red'], viag2))
else:
    print('Sua viagem foi de: {}{:.2f}Km{} então o preço vai ser: {}{:.2f}R$'
          .format(cor['verde'], viag, cor['branco'], cor['blue'], viag3))
