valores = list()
for cont in range(0, 4):
    valores.append(int(input('Digite um valor: ')))

print(valores)
for cont, v in enumerate(valores):
    print(f'{v} tem o índice {cont}')
print('Fim da lista')

