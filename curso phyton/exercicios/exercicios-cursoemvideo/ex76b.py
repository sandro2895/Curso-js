listagem = ('Lápis', 1.75,
            'Borracha', 2.0,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
espa = '-' * 50
print(f'<{espa}>')
for posi in range(0, len(listagem)):
    if posi % 2 == 0:
        print(f'{listagem[posi]:.<39}', end='')
    else:
        print(f'R${listagem[posi]:>9.2f}')
print(f'<{espa}>')
a