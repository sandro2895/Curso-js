nome = str(input('Qual é o seu nome? '))
nome = nome.title()
if nome == 'Doca':
    print('Que nome bonito')
elif nome == 'Paulo' or nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('seu nome é bem normal')
print('Bom dia {}!'.format(nome))
