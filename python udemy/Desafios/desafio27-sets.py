amigos1 = ['doca', 'romulo', 'paulo', 'joao', 'maria']
amigos2 = ['doca', 'romulo', 'marcelo', 'renato', 'eduardo', 'joao']
lista1 = set(amigos1).intersection(amigos2)  # Mostra que ambos valores estão na mesmas 2 listas
lista2 = set(amigos2).union(amigos1)
print(lista1)
print(lista2)