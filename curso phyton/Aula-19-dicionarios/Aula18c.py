estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for cont in brasil:
    for v in cont.values():
        print(v, end=' ')
    print()
    #for ke, va in cont.items():
        #print(f'{ke}: {va}')



