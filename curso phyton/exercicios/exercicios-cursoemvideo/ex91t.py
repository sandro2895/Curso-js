from random import randint
from time import sleep
from operator import itemgetter
dados = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('*', '=-=' * 11, '*')
for k, v in dados.items():
    print(f'    {k} Tirou {v} no dado.')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('*', '=-=' * 11, '*')
print('     ranking de jogadores')
for pos, cont in enumerate(ranking):
    print(f'{pos+1}º lugar o {cont[0]} que tirou {cont[1]}.')
print('*', '=-=' * 11, '*')


