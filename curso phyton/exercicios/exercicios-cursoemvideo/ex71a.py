print('=-=' * 15)
print('{:^43}'.format('Banco'))
print('=-=' * 15)
sac = int(input('Quanto você quer sacar? R$'))
total = sac
rest = 50
rcont = 0
while True:
    if total >= rest:
        total = total - rest
        rcont += 1
    else:
        if rcont > 0:
            print(f'{rcont} nota(s) de {rest}')
        if rest == 50:
            rest = 20
        elif rest == 20:
            rest = 10
        elif rest == 10:
            rest = 1
        rcont = 0
        if total == 0:
            break
