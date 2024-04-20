def contador(a, b, c):
    print('=-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1')
    for cont1 in range(1, 10 + 1):
        print(cont1, end=' ')
    print('FIM!')
    print('=-=' * 20)
    print('Contagem de 10 até 0 de 2 em 2')
    for cont2 in range(10, -1, -2):
        print(cont2, end=' ')
    print('FIM!')
    print('=-=' * 20)
    print('Agora é a sua vez de personalizar a contagem!')
    if c < 0:
        c *= -1
    elif c == 0:
        c = 1
    if a < b:
        cont = a
        while cont <= b:
            print(cont, end=' ')
            cont += c
    else:
        cont = a
        while cont >= b:
            print(cont, end=' ')
            cont -= c


# Programa principal
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
