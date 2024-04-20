carv = float(input("A quantos Km que o carro passou? "))
soma = carv - 80
somam = soma * 7
cor = {'nada': '\033[m',
       'cinza': '\033[4:37m',
       'red': '\033[4:31m'}

if carv > 80:
    print('Seu carro estava a: {}{:.1f}Km{} por hora. Você vai pagar uma multa de: {}{:.1f}R${}.'
          .format(cor['cinza'], carv, cor['nada'], cor['red'], somam, cor['nada']))
else:
    print('Seu carro estava a: {}{:.1f}Km{} por hora. Pode seguir em frente.'
          .format(cor['cinza'], carv, cor['nada']))
