def dobro(d, real=False):
    """
    Dobra o valor:
    param d: Valor digitado que será dobrado.
    param real: (Opcional) Retornará o valor formatado em cifrão real.
    return: valor dobrado
    """
    double = d * 2
    if real:
        return moeda(double)
    else:
        return float(double)


def metade(m, real=False):
    met = m / 2
    return float(met) if real is False else moeda(met)


def aumentar(a, p, real=False):
    aum = a * p / 100
    if real:
        return moeda(aum + a)
    return float(aum + a)


def diminuir(a, p, real=False):
    dim = a * p / 100
    if real:
        return moeda((dim - a) * -1)
    return float((dim - a) * -1)


def moeda(m):
    m = float(m)

    return f'R${m:.2f}'.replace('.', ',')


def titulo(t):
    l = '-' * len(t)
    print(f'[--{l}-----------]')
    print(f'       {t}')
    print(f'[--{l}-----------]')


def resumo(p=0, am=0, dim=0):
    titulo('RESUMO DO VALOR')
    return \
        f""" |Preço analisado:  {moeda(p)}|
 |Dobro do preço:   {moeda(dobro(p))}|
 |Metade do preço:  {moeda(metade(p))}|
 |{am}% de aumento:   {moeda(aumentar(p,am))}|
 |{dim}% de aumento:   {moeda(diminuir(p, dim))}|
[{'-' * 28}]
"""












