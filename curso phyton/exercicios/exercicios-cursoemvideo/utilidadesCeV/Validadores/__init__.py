def leiaInt(num):
    while True:
        try:
            msg = int(input(num))
        except(ValueError, TypeError):
            print('Número INTEIRO invalido!')
        except KeyboardInterrupt:
            return 'O Usuário interrompeu o programa.'
        else:
            return f'O número INTEIRO digitado foi: {msg}'


def leiaFloat(num):
    while True:
        try:
            msg = float(input(num))
        except(ValueError, TypeError):
            print('Número REAL invalido!')
        except KeyboardInterrupt:
            return 'O Usuário interrompeu o programa.'
        else:
            return f'O número REAL digitado foi: {msg}'
