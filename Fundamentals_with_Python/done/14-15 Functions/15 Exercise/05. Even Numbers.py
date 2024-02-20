def is_even(number: int) -> bool:
    return number % 2 == 0


def even_numbers(num_list: list) -> list:
    filtered = filter(is_even, num_list)
    filter_list = list(filtered)
    return filter_list


number_list = list(map(int, input().split()))
print(even_numbers(number_list))
