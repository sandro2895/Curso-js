import fibonacci
termosfb = int(input('Quantos termos quer mostrar? '))
while termosfb != 0:
    fibo = fibonacci.fibonacci(length=termosfb)
    print(fibo)
    termosfb = int(input('Quantos termos quer mostrar? '))
print('fim')



