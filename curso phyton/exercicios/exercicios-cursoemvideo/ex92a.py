from datetime import datetime
pessoa = {}
print('[', '=-=' * 12, ']')
pessoa['nome'] = str(input('Nome: '))
anonasc = int(input('Ano de nascimento: '))
pessoa['idade'] = (anonasc - datetime.now().year) * -1
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] <= 0:
    pessoa['ctps'] = 0
else:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    calc = (anonasc - pessoa['contratação']) * -1
    pessoa['Aposentadoria'] = calc + 35
print('[', '=-=' * 12, ']')
print('        ||', '---' * 5, '||')
print('*', '=-=' * 12, '*')
for k, v in pessoa.items():
    print(f'-   {k} tem o valor {v}')
print('*', '=-=' * 12, '*')

