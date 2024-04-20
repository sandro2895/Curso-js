import math
num1 = int(input('Digite um número para calcular seu fatorial: '))
multi = num1
fat = math.factorial(num1)
print('[', num1, end='')
while multi > 1:
    multi = multi - 1
    print(' x {}'.format(multi), end='')
print(' ] O fatorial de {} é igual a: {}'.format(num1, fat))
