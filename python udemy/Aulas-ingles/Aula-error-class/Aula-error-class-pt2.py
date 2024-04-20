def divide(dividend, divisor=1):
    if divisor == 0:
        raise ZeroDivisionError("Não pode ser dividido por zero")

    return dividend / divisor


students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]}

]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f'Name: {name} Grade {average}')
except ZeroDivisionError as e:
    print(f'There is no grade for {name} yet')
else:
    print('Grades Calculated')
finally:
    print('End of grades calculation')
