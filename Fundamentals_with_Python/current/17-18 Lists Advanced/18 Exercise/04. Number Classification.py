def filter_positive(numbers_):
    positives = [number for number in numbers_ if int(number) >= 0]
    return print(f'Positive: {", ".join(positives)}')


def filter_negative(numbers_):
    negatives = [number for number in numbers_ if int(number) < 0]
    return print(f'Negative: {", ".join(negatives)}')


def filter_even(numbers_):
    evens = [number for number in numbers_ if int(number) % 2 == 0]
    return print(f'Even: {", ".join(evens)}')


def filter_odd(numbers_):
    odds = [number for number in numbers_ if int(number) % 2 != 0]
    return print(f'Odd: {", ".join(odds)}')


numbers = input().split(", ")
filter_positive(numbers), filter_negative(numbers), filter_even(numbers), filter_odd(numbers)
