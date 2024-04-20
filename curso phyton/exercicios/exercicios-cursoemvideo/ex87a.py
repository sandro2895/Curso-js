matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = 0
somatc = 0
for linha in range(0, 3):
    for valor in range(0, 3):
        matriz[linha][valor] = int(input(f'Digite o valor para [{linha}, {valor}]: '))

for linha in range(0, 3):
    for valor in range(0, 3):
        print(f'[{matriz[linha][valor]:^5}]', end=' ')
    print()
for pos, num in enumerate(matriz):
    for num2 in num:
        if num2 % 2 == 0:
            somap += num2
print(f'A soma de todos os valores pares é: {somap}')
print(f'A soma de todos os valores da coluna3 é : {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é : {max(matriz[1])}')
