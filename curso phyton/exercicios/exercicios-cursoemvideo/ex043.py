altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.50:
    print('Você está abaixo do peso!')
elif imc >= 18.50 and imc < 25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está no sobrepeso!')
elif imc >= 30 and imc <= 40:
    print('Você está com obesidade!')
elif imc > 40:
    print('Você está com obesidade mórbida!')
