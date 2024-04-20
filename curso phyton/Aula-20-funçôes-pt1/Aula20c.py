def contador(*n):
    s = 0
    for cont in n:
        s += cont
    print(f'Somando os valores {n} temos {s}')


contador(2, 2)
contador(1, 2, 3)