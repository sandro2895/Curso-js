def pintar():
    while True:
        try:
            r = float(input('Qual é o rendimento da lata? '))
            a = float(input('Qual é a altura da parede? '))
            l = float(input('Qual é a largura da parede? '))
        except ValueError:
            print('Digite um valor em número Real ou Inteiro')
        else:
            alt_larg = a * l
            quant_latas = alt_larg / r
            print(f'Você precisa de: {quant_latas} latas de tinta')
            break


pintar()

