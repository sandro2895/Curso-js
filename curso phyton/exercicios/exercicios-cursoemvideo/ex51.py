pterm = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
decimterm = pterm + (10 - 1) * ra
conta = 0
for cont in range(pterm, decimterm + ra, ra):
    print('{}'.format(cont,), end=' -> ')
print('fim')
