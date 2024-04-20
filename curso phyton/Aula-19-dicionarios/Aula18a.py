pessoas = {'nome': 'Doca', 'idade': '28'}
pessoas['sexo'] = 'M'
pessoas['nome'] = 'Sandro'
print(pessoas)
del pessoas['sexo']
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
for pos, cont in pessoas.items():
    print(f'{pos} {cont}')

