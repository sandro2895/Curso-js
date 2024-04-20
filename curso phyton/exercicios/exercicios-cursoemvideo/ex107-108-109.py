import moeda
preco = int(input('Digite o preço : R$'))
print(f'O dobro de {moeda.moeda(preco)} é : {moeda.dobro(preco, real=True)}')
print(f'A metade de R${moeda.moeda(preco)} é : {moeda.metade(preco, real=True)}')
print(f'Aumentando 10%, temos: {moeda.aumentar(preco, 10, real=True)}')
print(f'Diminuindo em 13%, temos: {moeda.diminuir(preco, 13)}')
help(moeda.dobro)
