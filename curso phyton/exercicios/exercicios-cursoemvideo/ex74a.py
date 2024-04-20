import random
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
n3 = random.randint(1, 10)
n4 = random.randint(1, 10)
n5 = random.randint(1, 10)
lista = (n1, n1, n3, n4, n5)
cont = maior = menor = 0
for pos, c in enumerate(lista):
    if pos == 0:
        menor = c
        maior = c
    else:
        if c < menor:
            menor = c
        if c > maior:
            maior = c
print(f'Números sorteados: {lista[0]} {lista[1]} {lista[2]} {lista[3]} {lista[4]}')
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')