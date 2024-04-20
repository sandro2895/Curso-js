try:
    a = int(input('Numerador: '))
    d = int(input('Denominador: '))
    r = a / d
except Exception as error:
    print(f'ERRO!. O problema encontrado foi: {error.__class__}')
else:
    print(f'Resultado {r}')
finally:
    print('Fim do programa')