Words = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
         'mercado', 'programador', 'futuro')
for cont in Words:
    print(f'\nNa palavra {cont.upper()} temos: ', end=' ')
    for letra in cont:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

#PRATICAR