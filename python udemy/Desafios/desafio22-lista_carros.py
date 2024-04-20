carros = ['BMWX6', 'BMWI5', 'BMWI8']
pedido = str(input('Qual carro você deseja? ')).upper().strip().replace(' ', '')
if pedido in carros:
    print(f'{pedido} está disponível')
else:
    print('Desculpe, este carro não está disponível')
