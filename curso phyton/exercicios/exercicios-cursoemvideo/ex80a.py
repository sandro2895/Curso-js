valores = []
maior = 0
for pos, cont in enumerate(range(0, 5)):
    n1 = (int(input('Digite um valor: ')))
    if pos == 0 or n1 > valores[-1]:
        valores.append(n1)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if n1 <= valores[pos]:
                valores.insert(pos, n1)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1



print(valores)
