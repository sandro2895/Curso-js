import random
print('=-=' * 20)
print('                 Jogando Par ou impar')
print('=-=' * 20)
soma = cont = 0
result = ''
while True:
    jg = int(input('Digite um valor: '))
    qs = str(input('Será PAR ou IMPAR? [I/P]: ')).strip().upper()[0]
    if qs == 'I':
        qs = 'IMPAR'
    elif qs == 'P':
        qs = 'PAR'
    pc = random.randint(1, 10)
    soma = jg + pc
    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    print(f'Voce jogou: {jg}. E o pc jogou: {pc}. Somando o total deu: {soma} {result}!')
    if qs != result:
        break
    print('Voce venceu! Vamos jogar novamente..')
    print('=-=' * 20)
    cont = cont + 1
print('Você perdeu!')
print('=-=' * 20)
print(f'Total de vitorias : {cont}')


