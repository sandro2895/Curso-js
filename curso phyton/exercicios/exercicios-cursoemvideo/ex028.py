import time
import random
print('-=-' * 21)
print('Vou pensar em um número de 0 a 5. tente a adivinhar!')
print('-=-' * 21)
adv = int((input('O numero que eu escolho é: ')))
pct = random.randint(0, 5)
print('\033[1:32mPROCESSANDO...\033[m')
time.sleep(2)
if adv == pct:
    print('O número que eu pensei foi: \033[4m{}\033[m \033[1:36m Parabens você acertou! \033[m'.format(pct))
else:
    print('O número que eu pensei foi: \033[4m{}\033[m \033[1:31m Você errou! \033[m'.format(pct))
