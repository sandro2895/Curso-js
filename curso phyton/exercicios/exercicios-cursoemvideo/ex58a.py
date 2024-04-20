import random
numg1 = int(input('Estou pensando em um número de 1 a 10. Tente adivinhar: '))
numg2 = random.randint(1, 10)
tentativa = 1
while numg1 != numg2:
    numg1 = int(input('Tente novamente: '))
    tentativa = tentativa + 1
print('O número que eu pensei foi {}. Parabens você acertou'.format(numg2))
print('Foi necessário {} tentativa(s)!'.format(tentativa))
