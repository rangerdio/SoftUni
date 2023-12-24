def sorted_func(input_list: list) -> list:
    return sorted(input_list)


number_list = list(map(int, input().split()))
print(sorted_func(number_list))
