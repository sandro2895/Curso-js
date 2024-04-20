import random
al1 = input(str('Primeiro aluno: '))
al2 = input(str('Segundo aluno: '))
al3 = input(str('Terceiro aluno: '))
al4 = input(str('Quarto aluno: '))
alunos = [al1, al2, al3, al4]
random.shuffle(alunos)
print('A ordem dos alunos será: ')
print(alunos)
