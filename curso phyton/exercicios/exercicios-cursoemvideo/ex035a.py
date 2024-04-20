seg1 = float(input('Diga o primeiro segmento: '))
seg2 = float(input('Diga o segundo segmento: '))
seg3 = float(input('Diga o terceiro segmento: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg3 + seg2 > seg1:
    print('Pode formar um triângulo.')
else:
    print('Não pode formar um triângulo!')
if seg1 == seg2 and seg1 == seg3:
    print('O triângulo é EQUILÁTERO pois todos os lados são igual!')
elif seg1 == seg2 and seg1 != seg3 or seg1 == seg3 and seg1 != seg2 or seg2 == seg3 and seg2 != seg1:
    print('O triângulo é ISÓSCELES pois dois lados são igual e um é diferente!')
elif seg1 != seg2 and seg1 != seg3:
    print('O triângulo é ESCALENO pois todos os lados são diferentes!')
