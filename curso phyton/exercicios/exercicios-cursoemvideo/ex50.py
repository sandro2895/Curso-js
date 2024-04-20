soma = 0
conta = 0
for cont in range(1, 6 + 1):
    n1 = int(input('Digite o número '))
    if n1 % 2 == 0:
        conta = conta + 1
        soma = soma + n1
print('A soma de todos os números pares é: {}'.format(soma))
print('Você informou {} números par(s)'.format(conta))
