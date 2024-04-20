kms = float(input('Quantos quilômetros o carro percorreu? '))
dias1 = float(input('Por quantos dias o carro foi alugado? '))
kmp = kms * 0.15
diasp = dias1 * 60
totp = kmp + diasp

print('O carro percorreu {:.2f}Km e foi alugado por {:.2f} dias'.format(kms, dias1))
print('Então o  preço a pagar será de {:.2f}R$'.format(totp))
