matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):
    for val in range(0, 3):
        matriz[lin][val] = int(input(f'Digite o valor na posição [{lin}, {val}]: '))

for lin in range(0, 3):
    for val in range(0, 3):
        print(f'[{matriz[lin][val]:^5}]', end='')
    print()

