def calculation(n):
    return sum(map(int, str(abs(n))))


def count_of_digits(n):
    return len(str(abs(n)))


n = int(input('Введите число: '))
s, c = calculation(n), count_of_digits(n)
print(f'Сумма цифр: {s}\nКол-во цифр в числе: {c}\nРазность суммы и кол-ва цифр: {s - c}')