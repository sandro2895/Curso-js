sexo = str(input('Diga qual é o seu sexo? M/F: ')).strip().upper()[0]
print(sexo)
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos por favor diga qual é o seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))


