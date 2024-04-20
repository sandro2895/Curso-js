valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
valores2 = valores[:]
decre = valores.sort(reverse=True)
print(f'Os valores são: {valores2}')
print(f'Os valores em forma decrescente fica: {valores}')
print(f'Foram digitados {len(valores)} números na lista')
if 5 in valores:
    print('O valor 5 Foi digitado!')
else:
    print('O valor 5 não foi digitado!')
