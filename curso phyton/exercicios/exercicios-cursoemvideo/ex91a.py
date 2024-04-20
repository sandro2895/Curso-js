from time import sleep
from random import randint
from operator import itemgetter
jogs = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Dados sorteados:')
sleep(0.8)
for k, v in jogs.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.8)
ranking = sorted(jogs.items(), key=itemgetter(1), reverse=True)
print('*', '=-=' * 15, '*')
print('Ranking dos jogados')
print('*', '=-=' * 15, '*')
for k, v in enumerate(ranking):
    print(f' em {k+1}º lugar ficou {v[0]} com o valor: {v[1]}')
print('*', '=-=' * 15, '*')
