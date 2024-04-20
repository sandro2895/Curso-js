def fat(n=0, show=False):
    """
    -> Calcula o Fatorial de um número.
    :para n: O número a ser calculado.
    :para show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de n.

    """
    f = 1
    for cont in range(n, 0, -1):
        f *= cont
    if show:
        lista = []
        for pos, cont in enumerate(range(n, 0, -1)):
            lista.append(cont)
            if pos == 0:
                print(cont, end=' ')
            else:
                print(f'x {lista[pos]}', end=' ')
        return f'= {f}'

    else:
        return f


fato = fat(7, True)
print(fato)
help(fat)
