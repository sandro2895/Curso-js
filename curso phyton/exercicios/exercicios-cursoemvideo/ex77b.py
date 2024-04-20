words = ('programar', 'python', 'trabalhar', 'estudar', 'completo')
for cont in words:
    print(f'\nA palavra {cont} tem vogais:', end=' ')
    for palavras in cont:
        if palavras.lower() in 'aeiou':
            print(palavras, end=' ')
