def calculation():
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    operation = input('Введите знак операции: ')
    return a, b, operation


def operation_plus(a, b, operation):
    if operation == '+':
        rezult = a + b
        print(rezult)


a, b, operation = calculation()
operation_plus(a, b, operation)
