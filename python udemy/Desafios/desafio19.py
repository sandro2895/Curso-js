frutas = ['Maça', 'Uva', 'Sapoti', 'Maça', 'Manga', 'Maça', 'Maça']
num = 0
for fruta in frutas:
    print('[', fruta, end=' ] ')
    if 'Maça' in fruta:
        num += 1
print(f'\nO número de maça(s) é: {num}')
