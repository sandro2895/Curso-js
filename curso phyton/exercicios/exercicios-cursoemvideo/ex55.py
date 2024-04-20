maior = 0
menor = 0
for cont in range(1, 5+1):
    peso = float(input('O peso da {}ª pessoa: '.format(cont)))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('{}kg foi o MAIOR peso e {}kg foi o MENOR peso.'.format(maior, menor))
