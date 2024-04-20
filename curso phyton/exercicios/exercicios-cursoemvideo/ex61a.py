termo = int(input('O Primeiro termo da PA: '))
razao = int(input('Razao da PA: '))
decimtem = termo + (10 - 1) * razao
pa = termo
print(end='[ ')
print(termo, end=' > ')
while pa != decimtem:
    pa = pa + razao
    print(pa, end=' > ')
    if pa == decimtem:
        print(end='Fim ]')

