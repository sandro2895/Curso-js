numberes = []
pares = []
impares = []
while True:
    numberes.append(int((input('Digite um número: '))))
    resp = str(input('Quer continuar? ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Os valores são: {numberes}')
for pos, cont in enumerate(numberes):
    if cont % 2 == 0:
        pares.append(cont)
    else:
        impares.append(cont)
print(f'Somente os valores pares fica: {pares}')
print(f'Somente os valores impares fica: {impares}')

