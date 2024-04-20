while True:
    try:
        qs = float(input('Em qual temperatura a carne foi cozida? '))
    except ValueError:
        print('Digite um valor correto')

    else:

        if qs < 120:
            print("Cozinhar mais um pouco")
        if 120 <= qs < 130:
            print('Carne: Rare (Selada)')
            break
        if 130 <= qs < 140:
            print('Carne: Medium rare (Ao ponto para o mal)')
            break
        if 140 <= qs < 150:
            print('Carne: Medium (Ao ponto)')
            break
        if 150 <= qs < 160:
            print('Carne: Medium well (Ao ponto para o bem)')
            break
        if qs >= 160:
            print('Carne: Well done (Bem passada)')
            break

