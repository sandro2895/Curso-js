from utilidadesCeV import dado
from utilidadesCeV import moeda

dad = dado.leiaDinheiro('Digite o preço: R$')
a = moeda.resumo(dad, 10, 20)
print(a)
