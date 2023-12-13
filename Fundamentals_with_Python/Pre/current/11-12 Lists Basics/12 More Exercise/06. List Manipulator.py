my_list = list(map(int, "1 2 3 4 5".split()))
print(my_list)

while True:
    command = input()
    if command == "end":
        break
    command_list = command.split()
    print("command_list:", command_list)

    if command_list[0] == "exchange":
        index = int(command_list[1])
        if index < 0 or index >= len(my_list) - 1:
            print("Invalid index")
        else:
            sub_list_1 = my_list[:index + 1]
            sub_list_2 = my_list[index + 1:]
            sub_list_exchange = sub_list_2 + sub_list_1
            my_list = sub_list_exchange.copy()
            print(my_list)
    elif command_list[0] == "max" or command_list[0] == "min":
        even_list = []
        odd_list = []
        for element in my_list:
            if element % 2 == 0:
                even_list.append(element)
                even_list.sort(reverse=True)
            else:
                odd_list.append(element)
                odd_list.sort(reverse=True)
        print(even_list)
        print(odd_list)

        if command_list[1] == "even":
            if command_list[0] == "max":
                print(even_list[0])
            elif command_list[0] == "min":
                print(even_list[-1])

        elif command_list[1] == "odd":
            if command_list[0] == "max":
                print(odd_list[0])
            elif command_list[0] == "min":
                print(odd_list[-1])

