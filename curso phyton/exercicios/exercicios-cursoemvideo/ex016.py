import math
num1 = float(input('Diga um número: '))
numint1 = int(num1)
numint2 = math.floor(num1)
numint3 = num1 // 1
numint4 = math.trunc(num1)
print('O número real {} convertido para inteiro Usando int() é: {}'.format(num1, numint1))
print('O número real {} convertido para inteiro Usando math.floor() é: {}'.format(num1, numint2))
print('O número real {} convertido para inteiro Usando // 1 é: {}'.format(num1, numint3))
print('O número real {} convertido para inteiro Usando math.trunc() é: {}'.format(num1,numint4))
