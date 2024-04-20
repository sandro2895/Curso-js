import random

alu1 = input('Primeiro aluno: ')
alu2 = input('Segundo aluno: ')
alu3 = input('Terceiro aluno: ')
alu4 = input('Quarto aluno: ')
cor = {'nada': '\033[m',
       'red': '\033[31m',
       'blue': '\033[34m',
       'yellow': '\033[33m',
       'purple': '\033[7:30:45m'}
lunos = (alu1, alu2, alu3, alu4)
escol = random.choice(lunos)
if escol == alu1:
    print('O aluno escolhido foi: {}{}{}'
          .format(cor['red'], alu1, cor['nada']))
if escol == alu2:
    print('O aluno escolhido foi: {}{}{}'
          .format(cor['blue'], alu2, cor['nada']))
if escol == alu3:
    print('O aluno escolhido foi {}{}{}'
          .format(cor['yellow'], alu3, cor['nada']))
if escol == alu4:
    print('O aluno escolhido foi {}{}{}'
          .format(cor['purple'], alu4, cor['nada']))
