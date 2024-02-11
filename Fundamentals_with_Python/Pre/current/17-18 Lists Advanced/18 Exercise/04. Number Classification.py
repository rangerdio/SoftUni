def filter_positive(numbers_):
    return print(1)


def filter_negative(numbers_):
    return print(2)


def filter_even(numbers_):
    return print(3)


def filter_odd(numbers_):
    return print(4)


some_string = "1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33"
numbers = some_string.split(", ")
filter_positive(numbers), filter_negative(numbers), filter_even(numbers), filter_odd(numbers)
