valores = [10, 12, 34, 44, 57]


def remover20(x):
    return x > 20


mapear = list(map(remover20, valores))
filtrar = list(filter(remover20, valores))


print(mapear)
print(filtrar)
print(list(filter(lambda y: y <= 20, [10, 20, 30, 40, 50])))
