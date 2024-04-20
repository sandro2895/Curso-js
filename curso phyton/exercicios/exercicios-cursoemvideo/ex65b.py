end = False
soma = 0
quant = 0
maior = 0
menor = 0
media = 0
while not end:
    num = int(input('Digite outro número: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':
        end = True
media = soma / quant
print('A Quantidade de números foi: {}. E media entre os números é: {:.2f}'.format(quant, media))
print('O maior número foi: {}. E o menor número foi: {}'.format(maior, menor))
