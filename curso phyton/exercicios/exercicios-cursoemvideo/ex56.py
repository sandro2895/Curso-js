soma = 0
hvelho = 0
mnova = 0
idademe = 0
sexfem = 0
nome1 = ''
for cont in range(1, 5):
    nome = input('Qual é o seu nome? ')
    idade = int(input('Qual é a sua idade? '))
    sexo1 = input('Qual é o seu sexo? ')
    sexo2 = sexo1.upper()
    soma = soma + idade
    if cont == 1:
        hvelho = idade
        mnova = idade
        idademe = idade
        nome1 = nome
        if sexo2 == 'FEM':
            nome1 = 'Inexistente'
            hvelho = 0
        if sexo2 == 'FEM' and idade < 20:
            sexfem = sexfem + 1
    else:
        if idade > hvelho and sexo2 == 'MASC':
            hvelho = idade
            nome1 = nome
        if sexo2 == 'FEM' and idade < 20:
            sexfem = sexfem + 1
media = soma / 4
print('O homem mais velho é {} com {} anos'.format(nome1, hvelho))
print('No total {} mulheres tem menos de 20 anos de idade.'.format(sexfem))
print('A media de idade do grupo é de: {} Anos'.format(media))
