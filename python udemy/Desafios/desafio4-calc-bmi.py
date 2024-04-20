def imc(p=0, a=0):
    peso = p ** 2
    return a / peso


alt = float(input('Qual é sua altura? '))
pes = float(input('Qual é seu peso? '))
calc = imc(alt, pes)
print(f'{calc:.2f}')
if calc < 18.50:
    print('MAGREZA')
elif 18.50 <= calc <= 24.90:
    print('NORMAL')
elif 25 <= calc <= 29.90:
    print('SOBREPESO')
elif 30 <= calc <= 39.90:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')
