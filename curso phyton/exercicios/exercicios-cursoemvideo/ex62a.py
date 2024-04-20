primeiroterm = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
termos = primeiroterm
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        print(termos, end=' > ')
        cont = cont + 1
        termos = termos + razao
    print('PAUSE')
    mais = int(input('Quantos termos a mais você quer? '))
print('Fim')
