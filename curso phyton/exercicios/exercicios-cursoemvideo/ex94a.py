cadastr = {}
copia = []
qs = ''
cont = 0
soma = 0
while True:
    cadastr['nome'] = str(input('Nome: '))
    cadastr['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while cadastr['sexo'] not in 'FM':
        print('ERRO! Por favor, digite apenas M ou F.')
        cadastr['sexo'] = str(input('Sexo: ')).strip().upper()[0]
    cadastr['idade'] = int(input('Idade: '))
    copia.append(cadastr.copy())
    cont += 1
    soma += cadastr['idade']
    qs = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while qs not in 'SN':
        print('ERRO! responda apenas S ou N.')
        qs = str(input('Quer continuar? ')).strip().upper()[0]
    if qs == 'N':
        break
print('[', '=-=' * 15, ']')
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
print(f'B) A média de idade é de {soma / cont:.2f} anos.')
print('C) As Mulheres cadastradas foram ', end='')
for v in copia:
    if v['sexo'] == 'F':
        print(v['nome'], end=' ')
print('\nD) Lista das pessoas que estão acima da média:')
for k, v in enumerate(copia):
    if v["idade"] > soma / cont:
        print(f'    |nome = {v["nome"]}; sexo = {v["sexo"]}; idade = {v["idade"]};|')
print('[', '=-=' * 15, ']')

