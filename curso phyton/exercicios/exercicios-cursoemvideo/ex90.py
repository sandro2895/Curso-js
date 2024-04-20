notas = {}
notas['nome'] = str(input('Nome do aluno: '))
notas['media'] = float(input(f'Média de {notas["nome"]}: '))
print(f'Nome: {notas["nome"]}')
print(f'Média: {notas["media"]:.1f}')
if notas['media'] >= 7:
    notas['situacao'] = 'APROVADO!'
elif 5 <= notas['media'] < 7:
    notas['situacao'] = 'de RECUPERAÇÃO!'
else:
    notas['situacao'] = 'REPROVADO!'
print(f'O aluno {notas["nome"]} está {notas["situacao"]}')
print('-=-' * 20)
for k, v in notas.items():
    print(f'{k} é igual a {v}')

