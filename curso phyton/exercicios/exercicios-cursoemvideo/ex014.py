grau1 = float(input('Qual é a temperatura dessa sala em °C? '))
fahren = (grau1*9/5) + 32
cor = {'nada': '\033[m',
       'amarelo': '\033[7:30:43m',
       'red': '\033[7:30:41m'}
print('A temperatura de {}{:.2f}°C{} é igual a {}{:.2f}°F{}'
      .format(cor['amarelo'], grau1, cor['nada'], cor['red'], fahren, cor['nada']))
