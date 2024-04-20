# noinspection NonAsciiCharacters
def área(a, b):
    m = a * b
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {m:.1f}m².')


# Programa principal
print(' Controle de terrenos')
print('-' * 20)
larg = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))
área(larg, compr)
