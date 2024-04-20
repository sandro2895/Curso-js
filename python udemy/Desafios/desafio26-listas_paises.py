paises = {
          'Brasil': 'Brasilia',
          'Japão': 'Toquio',
          'Argentina': 'Buenos Aires',
          'Portugal': 'Lisboa',
          'Suecia': 'Estocolmo'
          }
qs = str(input('Digite o nome de um país: ')).capitalize()
if qs in paises:
    print(f'A capital de país {qs} é {paises[qs]}')
else:
    print('Desculpe, não temos informações sobre a capital desse país.')
