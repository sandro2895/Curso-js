soma = 0
num = 0
cont = 0
while num != 999:
    num = int(input('Digite número(s) Para somar. digite (999) Para parar. '))
    soma = soma + num
    cont = cont + 1
    if num == 999:
        cont = cont - 1
print('O valor total foi: {}'.format(soma - 999))
print('Foram digitados {} número(s)'.format(cont))
print('fim')
