try:
    valor = int(input('Digite um valor: '))
    print(f'valor digitado: {valor}')
except ValueError:
    print('Valor digitado incorreto!')
finally:
    print('codigo ok!')
#else:
   # soma = lambda x: x * 2
    #print(f'Valor multiplicado por 2: {soma(valor)}')
print('FIM')