import random
n = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
     random.randint(1, 10), random.randint(1, 10))
print(f'Os números sorteados foram {n[0]} {n[1]} {n[2]} {n[3]} {n[4]}')
print(f'O maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')

