# # index = 1
# # asd = [1, 2, 3, 4, 5, 6]
# #
# # print(asd[:5])
#
# asd = [2]
# def find_average_number(numbers: list):
#     if not numbers:
#         return "not_exist"
#     avr_number_index = len(numbers) // 2
#     return [numbers[avr_number_index], avr_number_index]
#
#
# print(find_average_number(asd)[0])


def get_elements_above_average(numbers: list, avr: float):
    above_avr = [element for element in numbers if element > avr]
    print(above_avr)
    return above_avr


asd = [-1, -2, -3, -4, -5, -6]
print(get_elements_above_average(asd, -3.5))
