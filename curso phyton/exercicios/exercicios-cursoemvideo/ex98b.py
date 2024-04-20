from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
contador(1, 10, 1)
print('Fim!')
contador(10, 0, 0)
print('Fim!')
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
