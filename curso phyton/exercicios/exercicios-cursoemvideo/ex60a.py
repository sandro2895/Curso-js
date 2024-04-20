fat = int(input('Digite um número para calcular seu fatorial: '))
mult1 = fat
mult2 = 0
mult3 = 0
while mult1 > 1:
    mult1 = mult1 - 1
    if mult1 == mult1:
        mult3 = mult1
        print(mult3)
    mult2 = mult1 * fat
    mult4 = mult3 * mult2
    print('{} x {} = {}'.format(fat, mult1, mult2))
print('O fatorial de: {} é igual a :{}'.format(fat, mult4))
