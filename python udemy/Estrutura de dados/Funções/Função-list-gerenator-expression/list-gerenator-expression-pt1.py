from sys import getsizeof
numeros = [item * 10 for item in range(100)]
print(type(numeros))

print(f'Números de bytes: {getsizeof(numeros)}')

print('='* 50)

numeros = (item * 10 for item in range(100))
print(type(numeros))

print(f'Números de bytes: {getsizeof(numeros)}')