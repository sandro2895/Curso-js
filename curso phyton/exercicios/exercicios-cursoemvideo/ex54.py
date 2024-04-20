import datetime
conta1 = 0
conta2 = 0
for cont in range(1, 7+1):
    nasc = int(input('em que ano a {}ª Pessoa nasceu:? '.format(cont)))
    data = datetime.date.today().year
    idade = data - nasc
    print('Você tem: {} de idade'.format(idade))
    if idade >= 18:
        print('Essa pessoa ja atingiu a maioridade')
        conta1 = conta1 + 1
    else:
        print('Essa pessoa ainda é menor de idade.')
        conta2 = conta2 + 1
print('{} Pessoas são maiores de idade e {} são menores de idade.'.format(conta1, conta2))
