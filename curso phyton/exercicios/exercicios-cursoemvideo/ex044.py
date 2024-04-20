compr = float(input('Qual foi o total da compra? R$'))
formp = float(input("""FORMAS DE PAGAMENTO
[ 1 ] á vista no dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a sua opção? """))
desc10 = compr * 10 / 100
descont10 = compr - desc10
desc5 = compr * 5 / 100
descont5 = compr - desc5
if formp == 1:
    print('O valor da compra de {:.1f}R$. A vista no dinheiro/cheque fica {:.1f}R$ com 10% porcento de desconto'.format(compr, descont10))
elif formp == 2:
    print('O valor da comprar de {:.1f}R$. A vista no cartão fica {:.1f}R$ com 5% porcento de desconto'.format(compr, descont5))
elif formp == 3:
    parc2 = compr / 2
    print('O valor fica como preço formal de {:.1f}R$. parcelado em 2 vezes que fica {:.1f}R$ cada parcela'.format(compr, parc2))
elif formp == 4:
    meses = int(input('Em quantos meses deseja pagar? 3 ou mais: '))
    if meses >= 3:
        juro20 = compr * 20 / 100
        mesesja = compr / meses
        jurosb = mesesja * 20 / 100
        jurostot = mesesja + jurosb
        mesestotj = compr + juro20
        print("""O valor parcelado em {} vezes fica com parcelas de {:.2f}R$ com 20% porcento em juros
e a compra de {:.2f}R$ vai custar um total de {:.2f}R$"""
              .format(meses, jurostot, compr, mesestotj))
    else:
        print('Número invalido tente novamente')
else:
    print('Número pedido invalido tente novamente.')