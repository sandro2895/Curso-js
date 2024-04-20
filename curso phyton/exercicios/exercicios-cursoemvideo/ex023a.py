num = int(input('Informe um número: '))
un = num // 1 % 10
dz = num // 10 % 10
ct = num // 100 % 10
ml = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(un))
print('Dezena: {}'.format(dz))
print('Centena: {}'.format(ct))
print('Milhar: {}'.format(ml))
