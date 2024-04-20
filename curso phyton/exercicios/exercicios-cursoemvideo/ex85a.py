temp = []
lista = []
for num in range(1, 7+1):
    temp.append(int(input('Digite um número: ')))
    lista.append(temp[:])
    temp.clear()
lista.sort()
print(f'Valores digitados:{lista}')
print(f'Somente os valores pares:', end='')
for pos, conta1 in enumerate(lista):
    if conta1[0] % 2 == 0:
        print(conta1, end=' ')
print(f'\nSomente os valores impares:', end='')
for conta2 in lista:
    if conta2[0] % 2 != 0:
        print(conta2, end=' ')


