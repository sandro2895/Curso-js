cidades = ('fortaleza', 'quixada', 'aquiraz')
qs = str(input('Digite o nome de uma cidade: ')).lower().strip().replace(' ','')
if qs in cidades:
    print(f'A cidade de {qs} está na lista!')
else:
    print(f'Essa cidade não está na lista!')
