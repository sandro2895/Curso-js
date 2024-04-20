from utilidades import *

arquiv = 'exemplo'
if not arquivexist(arquiv):
    arquivcriar(arquiv)
while True:
    qs = str(input('Abrir arquivo? ')).strip().upper()[0]
    if 'S' in qs:
        arquivabrir(arquiv)
        break

arq2 = ('exemplo abrir arquivo.txt')

arquivabrir(arq2)
