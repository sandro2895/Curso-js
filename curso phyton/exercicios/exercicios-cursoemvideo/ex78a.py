valor = []
for cont in range(0, 5):
    valor.append(int(input('Digite um valor: ')))

maior = max(valor)
menor = min(valor)
print(f'O maior valor é: {maior} E as suas posições são: ', end='')
for pos1, cont1 in enumerate(valor):
    if cont1 == maior:
        print(pos1, end='... ')
print(f'\nO menor valor é {menor} E as suas posições são: ', end='')
for pos2, cont2 in enumerate(valor):
    if cont2 == menor:
        print(pos2, end='... ')
