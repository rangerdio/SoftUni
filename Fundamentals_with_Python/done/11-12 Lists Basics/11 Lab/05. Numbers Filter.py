number_list = []
n = int(input())
for i in range(n):
    number_list.append(int(input()))

command = input()
for i in range(len(number_list) - 1, -1, -1):
    current_element = number_list[i]
    if command == "even":
        if current_element % 2 != 0:
            number_list.remove(current_element)
    elif command == "odd":
        if current_element % 2 == 0:
            number_list.remove(current_element)
    elif command == "negative":
        if current_element >= 0:
            number_list.remove(current_element)
    elif command == "positive":
        if current_element < 0:
            number_list.remove(current_element)
print(number_list)
