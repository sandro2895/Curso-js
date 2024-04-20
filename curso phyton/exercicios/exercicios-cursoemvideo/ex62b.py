ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
termo = ptermo
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        print(termo, end=' > ')
        cont = cont + 1
        termo = termo + razao
    print('PAUSE')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print('Foram mostrados {} Termos'.format(tot))
