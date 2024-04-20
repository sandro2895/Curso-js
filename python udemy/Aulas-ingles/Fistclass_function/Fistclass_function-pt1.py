def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculator(*values, operator):
    return operator(*values)


result = calculator(20, 20, operator=divide)
print(result)
