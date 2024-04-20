soma = contmil = menor = cont = 0
menorprod = ''

while True:
    prod = str(input('Produto: '))
    valor = float(input('Preço: '))
    cont += 1
    if cont == 1:
        menor = valor
        menorprod = prod
    else:
        if valor < menor:
            menor = valor
            menorprod = prod
    soma += valor
    if valor > 1000:
        contmil += 1
    quest = ' '
    while quest not in 'SN':
        quest = str(input('Mais alguma coisa? ')).strip().upper()[0]
    if quest == 'N':
        break
print(f'Total dos produtos: {soma:.2f}R$')
print(f'Total de produtos que valem mais de mil ReaisR$: {contmil}')
print(f'O nome do produtos mais barato é: {menorprod}')
