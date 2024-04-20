lista = []
notas = []
resp = ''
conta = 0
qt = ''
print('*', '=-=' * 12, '*')
print('          Médias dos alunos')
while True:
    lista.append(str(input('Nome do aluno: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    notas.append(lista[:])
    lista.clear()
    conta += 1
    resp = str(input('quer continuar? ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print('*', '=-=' * 12, '*')
med = 'MÉDIA'
nom = 'NOME'
print(f'No. {nom}           {med}')
for pos, cont in enumerate(notas):
    print(f'{pos:<3} {cont[0]:<15} {(cont[1] + cont[2]) / 2:.1f}')
print('*', '=-=' * 12, '*')

while True:
    print('___' * 13)
    qt = int(input('Quer ver a nota de qual aluno? '))
    if qt == 999:
        break
    if qt <= len(notas) - 1:
        print(f'Notas de {notas[qt][0]}: [{notas[qt][1]}, {notas[qt][2]}]')
print('___' * 13)












 #if pos < 1:
        #print((cont[1] + cont[2]) / 1.5,)





