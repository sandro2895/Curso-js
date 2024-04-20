soma = 0
for cont in range(1, 500 + 1, 2):
    if cont % 3 == 0:
        soma = soma + cont
print('Soma dos valores: {}'.format(soma))
