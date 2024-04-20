from math import hypot
catoposto = float(input('Qual é o comprimento do cateto oposto? '))
catjacente = float(input('Qual o comprimento do cateto adjacente? '))
hipo = catoposto ** 2 + catjacente ** 2
hipotot1 = hipo ** (1/2)
hipotot2 = hypot(catoposto, catjacente)
print('O cateto oposto sendo: {}'.format(catoposto))
print('O cateto adjacente sendo: {} '.format(catjacente))
print('O total da hipotenusa usando ** (1/2) é igual a: {:.2f}'.format(hipotot1))
print('O total da hipotenusa usando math.hypot é igual a: {:.2f}'.format(hipotot2))

