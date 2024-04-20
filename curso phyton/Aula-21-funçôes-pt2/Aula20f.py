def contador(i, f, p):
    """
    — > Faz uma contagem e mostra na tela.
    :para i: início da contagem
    :para f: final da contagem
    :para p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p


contador(0, 20, 1)
help(contador)

