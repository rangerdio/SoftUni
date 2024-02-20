number_list_strings = input().split()
number_list = [int(number_list_strings[index]) for index in range(len(number_list_strings))]
digits_to_remove = int(input())

for _ in range(digits_to_remove):
    number_list.remove(min(number_list))

number_list_as_string = [str(number_list[index]) for index in range(len(number_list))]
new_number_list_string = ", ".join(number_list_as_string)
print(new_number_list_string)
