#cont = 1
#while True:
    #print(cont, end=' ')
    #cont = cont + 1
n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma = soma + n
print(f'A soma vale {soma}')
