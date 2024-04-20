cont18 = conth = contfem20 = 0
while True:
    print('-=-' * 20)
    print('                 CADASTRO DE PESSOAS')
    print('-=-' * 20)
    idade = int(input('IDADE: '))
    if idade > 18:
        cont18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: ')).strip().upper()[0]
        if sexo == 'M':
            conth += 1
        elif idade < 20 and sexo == 'F':
            contfem20 += 1
    quest = ' '
    while quest not in 'NS':
        quest = str(input('Quer continuar? ')).strip().upper()[0]
    if quest == 'N':
        break
print('-=-' * 20)
print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Total de pessoas do sexo masculino: {conth}')
print(f'Total de pessoas do sexo feminino com menos de 20 anos: {contfem20}')


