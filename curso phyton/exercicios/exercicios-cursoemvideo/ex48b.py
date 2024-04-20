soma = 0
conta = 0
for cont in range(1, 500+1, 2):
    if cont % 3 == 0:
        conta = conta + 1
        soma = soma + cont
        print(cont, end=' ')

print('A soma de todos os números múltiplos de 3 é: {}'.format(soma))
print('Foram achados {} números'.format(conta))
