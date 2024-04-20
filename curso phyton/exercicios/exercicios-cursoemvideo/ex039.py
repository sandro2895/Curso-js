import datetime

nasc = float(input('Qual é o ano do seu nascimento? '))
nasc = int(nasc)
data = datetime.date.today().year
print(data)
idade = nasc - data
print(idade)
idade2 = idade + 18
print(idade2)
idade3 = nasc + 18
idade4 = idade2 * -1
print(idade3)
print(idade4)
if idade > -18:
    print("""Você não precisa se alistar ainda Pois ainda falta {} ano(s) para você se alistar.
Seu alistamento será em {}."""
          .format(idade2, idade3))
elif idade == -18:
    print('Você precisa se alistar agora mesmo!')
elif idade < -18:
    print(""""Ja fazem {} ano(s) que você deveria ter se alistado!
Seu alistamento foi em {}.""".format(idade4, idade3))
