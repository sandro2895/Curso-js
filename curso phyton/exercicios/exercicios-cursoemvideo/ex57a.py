sexo = ''
nome = ''
while sexo != 'M' and sexo != 'F':
    nome = str(input('Qual é o seu nome? ')).title()
    sexo = str(input('Qual é o seu sexo? M/F: ')).strip().upper()[0]
    print(sexo)
if sexo == 'M':
    sexo = 'Masculino'
if sexo == 'F':
    sexo = 'Feminino'
print('O seu nome é {} e seu sexo é: {}'.format(nome, sexo))
