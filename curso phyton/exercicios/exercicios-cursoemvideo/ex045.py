import random
import time
cor = {'nada': '\033[m',
       'azul': '\033[36m',
       'red': '\033[31m',
       'green': '\033[32m',
       'roxo': '\033[35m'}

escolhUS1 = int(input("""Vamos jogar pedra, papel e tesoura!
         Suas opções:
[ 1 ]PEDRA  [ 2 ]PAPEL  [ 3 ]TESOURA    
Sua escolha: """))
escolhas = ('PEDRA', 'PAPEL', 'TESOURA')
escolhUS2 = ''
escolhaPC = random.choice(escolhas)
if escolhUS1 == 1:
    escolhUS2 = 'PEDRA'
    print('Eu escolho {}!'.format(escolhUS2))
elif escolhUS1 == 2:
    escolhUS2 = 'PAPEL'
    print('Eu escolho {}!'.format(escolhUS2))
elif escolhUS1 == 3:
    escolhUS2 = 'TESOURA'
    print('Eu escolho {}!'.format(escolhUS2))
else:
    print('{}Número invalido tente novamente!{}'.format(cor['red'], cor['nada']))
print('PROCESSANDO...')
#time.sleep(2)
print('O pc escolhe {}!'.format(escolhaPC))
if escolhaPC == 'PEDRA' and escolhUS2 == 'TESOURA':
    print('{} vence {} você perdeu!'.format(escolhaPC, escolhUS2))
if escolhaPC == 'PEDRA' and escolhUS2 == 'PEDRA':
    print('{} e {} são iguais foi um empate!'.format(escolhaPC, escolhUS2))
if escolhaPC == 'PEDRA' and escolhUS2 == 'PAPEL':
    print('{} vence {} você ganhou!'.format(escolhUS2, escolhaPC))
if escolhaPC == 'TESOURA' and escolhUS2 == 'PAPEL':
    print('{} vence {} você perdeu!'.format(escolhaPC, escolhUS2))
if escolhaPC == 'TESOURA' and escolhUS2 == 'TESOURA':
    print('{} e {} são iguais foi um empate!'.format(escolhaPC, escolhUS2))
if escolhaPC == 'TESOURA' and escolhUS2 == 'PEDRA':
    print('{} vence {} você venceu!'.format(escolhUS2, escolhaPC))
if escolhaPC == 'PAPEL' and escolhUS2 == 'PEDRA':
    print('{} vence {} você perdeu!'.format(escolhaPC, escolhUS2))
if escolhaPC == 'PAPEL' and escolhUS2 == 'PAPEL':
    print('{} e {} são iguais foi empate!'.format(escolhaPC, escolhUS2))
if escolhaPC == 'PAPEL' and escolhUS2 == 'TESOURA':
    print('{} vence {} você venceu!'.format(escolhUS2, escolhaPC))

