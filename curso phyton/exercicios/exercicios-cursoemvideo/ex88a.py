from random import randint
from time import sleep
lista = []
jogo = []
tot = 0
print('[', '=-=' * 4, 'MEGA SENA', '=-=' * 4, ']')
jg = int(input('Quantos jogos de 6 da MEGA SENA? '))
while tot < jg:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    jogo.append(lista[:])
    lista.clear()
    tot += 1
for pos, conta in enumerate(jogo):
    sleep(1)
    print(f'jogo {pos+1}:{conta}')
sleep(0.5)
print('[', '=-=' * 5, 'FIM', '=-=' * 5, ']')


