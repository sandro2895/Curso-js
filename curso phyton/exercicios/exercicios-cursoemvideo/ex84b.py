pessoas = []
cadastro = []
leve = []
pesado = []
maior = menor = 0
quest = ''
contcad = 0
while True:
    pessoas.append(str(input('Nome da pessoa: ')))
    pessoas.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        maior = pessoas[1]
        menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    cadastro.append(pessoas[:])
    contcad += 1
    pessoas.clear()
    quest = str(input('Quer continuar? ')).strip().upper()[0]
    while quest not in 'SN':
        quest = str(input('Quer continuar? ')).strip().upper()[0]
    if quest == 'N':
        break
print(f'Foram {contcad} pessoas cadastradas')
print(f'Pessoas mais pesadas cadastradas:', end=' ')
for pos1, cont1 in enumerate(cadastro):
    if cont1[1] == maior:
        print(cont1[0], end=' ')
print(f'\nPessoas mais leves cadastradas', end=' ')
for cont2 in cadastro:
    if cont2[1] == menor:
        print(cont2[0], end=' ')


