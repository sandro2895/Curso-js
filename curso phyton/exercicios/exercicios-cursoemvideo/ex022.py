nome1 = str(input('Diga o seu nome completo: '))
test = nome1.replace(' ', '')
print(test)
maiusnome = nome1.upper()
minusnome = nome1.lower()
nome2 = len(nome1.replace(' ', ''))
divd = nome1.split()
nletras1 = divd[0]
ler = len(divd[0])
print(ler)
print('-Seu nome em letras maiúsculas é: {}'.format(maiusnome))
print('-Seu nome em letras minúsculas é: {}'.format(minusnome))
print('-Seu nome completo tem o total de: {} Letras'.format(nome2))
print('-Seu primeiro nome é: {}'.format(nletras1))

