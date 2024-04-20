pessoas = []
cadastro = []
leve = []
pesado = []
quest = ''
contcad = 0
while True:
    pessoas.append(str(input('Nome da pessoa: ')))
    pessoas.append(int(input('Peso: ')))
    cadastro.append(pessoas[:])
    contcad += 1
    pessoas.clear()
    quest = str(input('Quer continuar? ')).strip().upper()[0]
    while quest not in 'SN':
        quest = str(input('Quer continuar? ')).strip().upper()[0]
    if quest == 'N':
        break
for conta in cadastro:
    if conta[1] >= 100:
        pesado.append(conta[0])
    else:
        leve.append(conta[0])
print(f'Pessoas pesadas:', end=' ')
for p in pesado:
    print(p, end=' ')
print(f'\nPessoas leves:', end=' ')
for l in leve:
    print(l, end=' ')
print('\n')
print(f'Total de pessoas cadastradas {contcad}')
