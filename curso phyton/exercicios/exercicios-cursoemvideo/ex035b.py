seg1 = float(input('Diga o primeiro segmento: '))
seg2 = float(input('Diga o segundo segmento: '))
seg3 = float(input('Diga o terceiro segmento: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg3 + seg2 > seg1:
    print('Pode formar um triângulo.')
    if seg1 == seg2 == seg3:
        print('O triângulo é EQUILÁTERO')
    if seg1 != seg2 != seg3 != seg1:
        print('O triângulo é ESCALENO')
    if seg1 == seg2 and seg1 != seg3 or seg1 == seg3 and seg1 != seg2 or seg2 == seg3 and seg2 != seg1:
        print('O triangulo é ISÓSCELES')
else:
    print('Não pode formar um triângulo!')
