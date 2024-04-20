real = float(input('Quantos reais voce tem? R$'))
cor = {'nada': '\033[m',
         'verde': '\033[4:32m',
         'vermelho': '\033[4:31m',
         'azul': '\033[4:36m',
         'amarelo': '\033[4:33m'}
print('Com {}R${:.2f} Real(s){} você pode comprar {}US${:.2f} Dólares{}'
      .format(cor['verde'], real, cor['nada'], cor['amarelo'], real*0.20949, cor['nada']))
print('Com {}R${:.2f} Real(s){} você pode comprar {}€{} Euros{}'
      .format(cor['verde'], real, cor['nada'], cor['azul'], real*0.19121, cor['nada']))
print('Com {}R${:.2f} Real(s){} você pode comprar {}¥{} Iene(s){}'
      .format(cor['verde'], real, cor['nada'], cor['vermelho'], real*29.9401, cor['nada']))
