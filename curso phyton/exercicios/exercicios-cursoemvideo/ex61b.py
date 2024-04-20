ptermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = ptermo
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end=' ')
    termo = termo + razao
    cont = cont + 1


