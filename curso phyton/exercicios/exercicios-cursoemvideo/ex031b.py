dist1 = float(input('Qual a distancia da viagem? '))


preco = dist1 * 0.50 if dist1 <= 200 else dist1 * 0.45

print('A sua viagem foi de {:.2f}Km então o preço vai ser de: {:.2f}R$'
      .format(dist1, preco))
