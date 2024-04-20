try:
    a = int(input('Numerador: '))
    d = int(input('Denominador: '))
    r = a / d
except:
    print('ERRO!')
else:
    print(f'Resultado {r}')
finally:
    print('Fim do programa')

