soma = cont = 0
while True:
    num = int(input('Digite números para somar (Digite 999 para parar): '))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print(f'A quantidade de números que você digitou foi: {cont}')
print(f'A soma de todos os números é igual a: {soma}')
