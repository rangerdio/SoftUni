number_list = input().split()
message = input()
# print(number_list)
# print(message)
mark = False

for index in range(len(number_list)):
    sum_letters_int = 0
    for letter in number_list[index]:
        sum_letters_int += int(letter)
    number_list[index] = str(sum_letters_int)
# print()
# print(number_list)
# print(message)
# print(len(message))

for index in range(len(number_list)):
    element = number_list[index]
    element_print = int(element)
    while element_print > len(message) - 1:
        element_print -= (len(message))

    if mark:
        print(f"{message[element_print]}", end="")
        mark = False
    else:
        print(f"{message[element_print + index]}", end="")  # Why! without + index Results are terrible
print()
