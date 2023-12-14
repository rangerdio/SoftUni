string = input()
my_list = list(map(int, string.split()))
# print(my_list)

while True:
    command = input()
    if command == "end":
        break
    command_list = command.split()

    # start pre-checks
    # If "even" or "odd" in command_list, then verify existence of Even and Odd, which will be used on few places
    even_list = []
    odd_list = []
    for element in my_list:
        if element % 2 == 0:
            even_list.append(element)
            even_list.sort(reverse=True)
        else:
            odd_list.append(element)
            odd_list.sort(reverse=True)
    # confirm existence of even and odd max/min
    even_exist = True if len(even_list) > 0 else False
    odd_exist = True if len(odd_list) > 0 else False
    # end pre-checks

    if command_list[0] == "exchange":
        index = int(command_list[1])
        if index < 0 or index > len(my_list) - 1:
            print("Invalid index")
        else:
            sub_list_1 = my_list[:index + 1]
            sub_list_2 = my_list[index + 1:]
            sub_list_exchange = sub_list_2 + sub_list_1
            my_list = sub_list_exchange.copy()

    #  Find Min/Max even/odd number
    elif command_list[0] == "max" or command_list[0] == "min":

        # Finding  Even target if exists or print no watches
        if command_list[1] == "even":
            if (command_list[0] == "max" or command_list[0] == "min") and not even_exist:
                print("No matches")

            elif command_list[0] == "max":
                max_even = even_list[0]
                # if there are one, or more than one max even print most right one
                if my_list.count(max_even) >= 1:
                    for index in range(-1, -len(my_list) - 2, -1):
                        if my_list[index] == max_even:
                            print(index + len(my_list))
                            break
            elif command_list[0] == "min":
                min_even = even_list[-1]
                # if there are more than one min even, print most right one
                if my_list.count(min_even) >= 1:
                    for index in range(-1, -len(my_list) - 2, -1):
                        if my_list[index] == min_even:
                            print(index + len(my_list))
                            break

        # Finding  Odd target if exists, or print no matches
        elif command_list[1] == "odd":
            if (command_list[0] == "max" or command_list[0] == "min") and not odd_exist:
                print("No matches")
            elif command_list[0] == "max":
                max_odd = odd_list[0]
                # if there are more than one max odd, print the most right one, if one print only 1
                if my_list.count(max_odd) >= 1:
                    for index in range(-1, -len(my_list) - 2, -1):
                        if my_list[index] == max_odd:
                            print(index + len(my_list))
                            break
            elif command_list[0] == "min":
                min_odd = odd_list[-1]
                # if there are more than one max odd, print the most right one, if one, print only 1
                if my_list.count(min_odd) >= 1:
                    for index in range(-1, -len(my_list) - 2, -1):  # len=4 (i 0123),but when - it is -4 -2 for index(0)
                        if my_list[index] == min_odd:
                            print(index + len(my_list))
                            break

    elif command_list[0] == "first":
        count = int(command_list[1])
        type_command = command_list[2]
        # if count is greater than the list itself, invalid count
        if count > len(my_list):
            print("Invalid count")
        # if zero, []

        elif type_command == "even" and not even_exist:
            print(even_list)
        elif type_command == "odd" and not odd_exist:
            print(odd_list)
        else:
            if type_command == "even":
                first_evens = []
                for element in my_list:
                    if element % 2 == 0:
                        first_evens.append(element)
                if len(first_evens) < count:    # If not enough elements to satisfy the count, print as many as you can
                    print(first_evens)
                elif len(first_evens) >= count:     # if hits are more than the count request , print the counted only
                    first_evens_limit_to_count = []
                    for index in range(count):
                        first_evens_limit_to_count.append(first_evens[index])
                    print(first_evens_limit_to_count)
            elif type_command == "odd":
                first_odds = []
                for element in my_list:
                    if element % 2 != 0:
                        first_odds.append(element)
                if len(first_odds) < count:    # If not enough elements to satisfy the count, print as many as you can
                    print(first_odds)
                elif len(first_odds) >= count:     # if hits are more than the count request, print the counted only
                    first_odds_limit_to_count = []
                    for index in range(count):
                        first_odds_limit_to_count.append(first_odds[index])
                    print(first_odds_limit_to_count)

    elif command_list[0] == "last":
        count = int(command_list[1])
        type_command = command_list[2]
        # if count is greater than the list itself
        if count > len(my_list):
            print("Invalid count")
        # if zero
        elif type_command == "even" and not even_exist:
            print(even_list)
        elif type_command == "odd" and not odd_exist:
            print(odd_list)
        else:
            if type_command == "even":
                last_evens = []
                for element in my_list:
                    if element % 2 == 0:
                        last_evens.append(element)
                if len(last_evens) <= count:  # If not enough elements to satisfy the count, print as many as you can !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!changed with =
                    print(last_evens)
                elif len(last_evens) >= count:  # if hits are more than the count request , print the counted only
                    last_evens_limit_to_count = []
                    for index in range(len(last_evens) - count, len(last_evens)):
                        last_evens_limit_to_count.append(last_evens[index])
                    print(last_evens_limit_to_count)

            elif type_command == "odd":
                last_odds = []
                for element in my_list:
                    if element % 2 != 0:
                        last_odds.append(element)
                if len(last_odds) <= count:  # If not enough elements to satisfy the count, print as many as you can            changed the above to look like this
                    print(last_odds)
                elif len(last_odds) > count:  # if hits are more than the count request, print the counted only
                    last_odds_limit_to_count = []
                    for index in range(len(last_odds) - count, len(last_odds)):
                        last_odds_limit_to_count.append(last_odds[index])
                    print(last_odds_limit_to_count)
print(my_list)
