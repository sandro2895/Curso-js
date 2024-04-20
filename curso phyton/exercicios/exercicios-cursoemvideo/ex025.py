nome1 = str(input('Qual é o seu nome completo? '))
nome2 = nome1.title()
nome3 = nome2.strip()
test = 'Silva' in nome3
print('-Se o seu nome tem Silva? a resposta é: {}'.format(test))
