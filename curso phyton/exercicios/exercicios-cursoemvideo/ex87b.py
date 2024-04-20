matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for lin in range(0, 3):
    for num in range(0, 3):
        matriz[lin][num] = int(input(f'Digite um valor para a posição [{lin}, {num}]: '))

for lin in range(0, 3):
    for num in range(0, 3):
        print(f'[{matriz[lin][num]:^5}]', end='')
        if matriz[lin][num] % 2 == 0:
            spar += matriz[lin][num]
    print()
print(f'Valores pares somados: {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'Soma dos valores da terceira coluna: {scol}')
for c in range(0, 3):
    if c == 0:
        mai += matriz[1][c]
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]
print(f'O maior valor da linha 2 é: {mai}')


