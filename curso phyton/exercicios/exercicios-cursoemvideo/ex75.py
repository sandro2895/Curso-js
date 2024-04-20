
numbers = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))
cont9 = numbers.count(9)
print(f'Os valores digitados foram {numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]}')
print(f'O valor 9 apareceu {cont9} Vez(s)!')
if 3 in numbers:
    print(f'O número 3 apareceu pela primeira vez na posição: {numbers.index(3)+1}')
else:
    print(f'O número 3 Nunca apareceu')
print('Números pares encontrados foram:', end=' ')
for cont in numbers:
    if cont % 2 == 0:
        print(cont, end=' ')


