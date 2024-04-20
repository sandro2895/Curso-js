try:
    a = int(input('Numerador: '))
    d = int(input('Denominador: '))
    r = a / d
except(ValueError, TypeError):
    print('ERRO! Valor digitado incorreto!')

except ZeroDivisionError:
    print('ERRO! Não pode ser dividido por 0.')

except KeyboardInterrupt:
    print('ERRO! Usuário interrompeu a digitação dos valores.')

except Exception as error:
    print(f'A causa do erro foi! {error.__cause__}')

else:
    print(f'Resultado {r}')
finally:
    print('Fim do programa')