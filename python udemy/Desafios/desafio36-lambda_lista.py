quadrado = lambda n: n ** 2
lista = [1, 2, 3, 4, 5, 6]
resu = []
for n in lista:
    print(f'[= {quadrado(n)}', end=' =] ')
    resu.append(quadrado(n))
print(f'\nOs quadrados da lista {lista} é: {resu}')
