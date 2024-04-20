nome1 = input('Nome do aluno: ')
nota1 = float(input('Qual foi a primeira nota? '))
nota2 = float(input('Qual foi a primeira nota? '))
media = (nota1 + nota2)/2
print('A primeira nota foi {:.1f}'.format(nota1))
print('A segunda nota foi {:.1f}'.format(nota2))
cor = {'nada': '\033[m',
       'red': '\033[4:31m',
       'verdb': '\033[4:92m',
       'verde': '\033[4:32m',
       'redb': '\033[4:91m'}
if media >= 7:
    print('A média do aluno {} é: {}{:.1f}{}. {}Parabens você passou{}.'
          .format(nome1, cor['verdb'], media, cor['nada'], cor['verde'], cor['nada']))
else:
    print('A média do aluno {} é: {}{:.1f}{}. {}Infelizmente você não passou{}.'
          .format(nome1, cor['redb'], media, cor['nada'], cor['red'], cor['nada']))

