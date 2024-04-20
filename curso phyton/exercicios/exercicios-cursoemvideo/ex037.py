num = int(input('Digite um número para converter: '))
conv = float(input('Agora digite 1 para converter o número para binário ou 2 para octal ou 3 para hexadecimal. '))

conv1 = int(conv)

if conv == 1:
    bina = bin(num)
    print('O número {} convertido para binario é: {}'.format(num, bina[2:]))
elif conv == 2:
    octl = oct(num)
    print('O número {} convertido para octal é: {}'.format(num, octl[2:]))
elif conv == 3:
    hexe = hex(num)
    print('O número {} convertido para hexadecimal é: {}'.format(num, hexe[2:].upper()))
else:
    print('Número para conversão incorreto. Tente novamente')
