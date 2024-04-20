valor = int(input('Valor a ser sacado: '))
tot = valor
saque = 50
Ncont = 0
while True:
    if tot >= saque:
        tot -= saque
        Ncont += 1
    else:
        if Ncont != 0:
            print(f'{Ncont} Notas de {saque}R$')
        if saque == 50:
            saque = 20
        elif saque == 20:
            saque = 10
        elif saque == 10:
            saque = 1
        Ncont = 0
        if tot == 0:
            break
