resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
media = soma / quant
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
print('Você digitou {} números. A media entre eles foi: {:.2f}'.format(quant, media))
