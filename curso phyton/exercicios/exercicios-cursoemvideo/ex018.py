from math import radians, sin, cos, tan
ang = float(input('Digite um angulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('seno: {:.2f}'.format(sen))
print('cosseno {:.2f}'.format(cos))
print('tangente {:.2f}'.format(tan))
