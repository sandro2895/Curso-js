def leiaDinheiro(msg):
    while True:
        resp = str(input(msg)).replace(',', '.').strip()
        if resp.isalpha() or resp == '':
            print(f'\033[31mErro! "{resp}" não é um valor valido!\033[m')
        else:
            return float(resp)







