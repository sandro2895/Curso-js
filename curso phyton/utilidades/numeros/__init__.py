def fat(n):
    """
      -> Total do fatorial de um número
      para n: Número digitado para o fatorial
      return: Retorna o fatorial do número digitado.
    """
    f = 1
    for cont in range(1, n + 1):
        f *= cont
    return f
