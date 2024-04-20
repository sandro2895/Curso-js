nome = input('Nome do aluno: ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(media)
if media < 5.0:
    print('O Aluno foi reprovado!')
elif media >= 5.0 and media <= 6.9:
    print('O aluno está de recuperação!')
elif media >= 7.0:
    print('O aluno foi aprovado!')