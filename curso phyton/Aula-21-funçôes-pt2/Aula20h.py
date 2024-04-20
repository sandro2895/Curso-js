# def test():
# n = 9
# print(f'O Valor de n dentro(local) vale: {n}')


# n = 7
# print(f'O valor n fora(global) vale: {n}')
# test()


def testa(b):
    global a
    b += 2
    a = 9
    print(b)
    print(a)


a = 6
testa(a)

