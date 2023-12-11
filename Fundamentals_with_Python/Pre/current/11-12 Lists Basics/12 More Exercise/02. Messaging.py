number_list = input().split()
message = input()

for index in range(len(number_list)):
    sum_letters_int = 0
    for letter in number_list[index]:
        sum_letters_int += int(letter)
    number_list[index] = str(sum_letters_int)

for index in range(len(number_list)):
    element = number_list[index]
    element_print = int(element)
    while element_print > len(message) - 1:
        element_print -= (len(message))

    print(f"{message[element_print]}", end="")
    message = message[:element_print] + message[element_print + 1:]
