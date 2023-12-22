def sum_numbers(num_1: int, num_2:int) -> int:
    return num_1 + num_2


def subtract(num_1: int, num_3: int) -> int:
    return num_1 - num_3


def add_and_subtract(num_1: int, num_2: int, num_3: int) -> int:
    returned_result = sum_numbers(num_1, num_2)
    return subtract(returned_result, num_3)


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(add_and_subtract(number_1, number_2, number_3))
