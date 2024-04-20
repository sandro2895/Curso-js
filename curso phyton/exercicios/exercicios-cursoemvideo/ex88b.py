import random
lista = []
jogos = []
print('=-=' * 25)
print('                              MEGA SENA')
print('=-=' * 25)
jg = int(input('Quantos jogos da mega sena? '))
tot = 0
while tot < jg:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=-' * 8, f'Sorteando {jg} Jogo(s)', '-=-' * 10)
for pos, cont in enumerate(jogos):
    print(f' Jogo {pos +1}:{cont}')

