def find_average_number(numbers: list):
    total = 0
    for element in numbers:
        total += element
    return total / len(numbers)


def get_elements_above_average(numbers: list, avr: float):
    # print(f"input number list: {numbers}")
    # print(f"average number in 'get_elements_above_average': {average}")
    above_avr = [element for element in numbers if element > avr]
    # print(above_avr)
    return above_avr


number_list = list(map(int, input().split()))
number_of_elements = len(number_list)
average = find_average_number(number_list)
# print(f"average number is: {average}")


numbers_above_average_list = get_elements_above_average(number_list, average)
numbers_above_average_list.sort(reverse=True)
numbers_above_average_list_strings = [str(element) for element in numbers_above_average_list]

if not numbers_above_average_list:
    print("No")
elif len(numbers_above_average_list_strings) <= 5:    # LESS THAN 5 Nums ABOVE AVERAGE
    print(" ".join(numbers_above_average_list_strings))
else:   # MORE THAN 5 Nums ABOVE AVERAGE
    print(" ".join(numbers_above_average_list_strings[:5]))
