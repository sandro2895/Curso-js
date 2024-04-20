#galera = [['João', 32], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#for p in galera:
   # print(f'{p[0]} Tem {p[1]} anos de idade!')

galera = []
dados = []
for c in range(0, 3):
    dados.append(str(input('Qual é o seu nome? ')))
    dados.append(int(input('Qual é sua idade? ')))
    galera.append(dados[:])
    dados.clear()

print(galera)

for p in galera:
    if p[1] > 27:
        print(f'{p[0]} tem mais de 27 anos')
    else:
        print(f'{p[0]} tem menos de 27 anos!')
