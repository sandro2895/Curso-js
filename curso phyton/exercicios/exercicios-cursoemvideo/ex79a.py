numberes = []
quest = ''
while True:
    n = int(input('Digite um número: '))
    if n not in numberes:
        numberes.append(n)
    else:
        print('Número duplicado. não sera adicionado!')
    quest = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while quest not in 'SN':
        quest = str(input('Quer continuar adicionando? [S/N] ')).strip().upper()[0]
    if quest == 'N':
        break
numberes.sort()
print(numberes)

