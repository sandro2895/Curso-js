nome1 = str(input('Qual é o seu nome? '))
nome2 = nome1.title()

if nome2 == 'Gustavo':
    print('Que nome legal!')
else:
    print('Seu nome é tão normal')
print('Bom dia {}'.format(nome2))


