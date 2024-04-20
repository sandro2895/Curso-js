def divide(dividend, divisor=1):
    if divisor == 0:
        raise ZeroDivisionError("Não pode ser dividido por zero")

    return dividend / divisor


grades = []

print("Welcome to the avarage grade program")
try:
    avarage = divide(sum(grades), len(grades))
    print(f'A nota media é {avarage}')
except ZeroDivisionError as e:

    print('There is no grades yet on your list')
else:
    print(avarage)
finally:
    print('End of program')

