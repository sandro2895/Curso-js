num = [[], []]
valor = 0
for cont in range(1, 7+1):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)

    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Todos os valores {num}')
print(f'Valores pares:{num[0]}')
print(f'Valores impares:{num[1]}')

