def is_winning(ticket):
    winner = False
    left = ticket[:10]
    right = ticket[10:]
    left_counter = 1
    right_counter = 1
    # left_symbol = ""
    # right_symbol = ""
    symbol = ""
    left_dict = {}
    right_dict = {}
    for index in range(len(left)):
        if index == len(left) - 1:
            if left[index] == left[index - 1]:
                left_dict[left[index]] = left_counter
            else:
                left_dict[left[index]] = left_counter
                left_dict[left[index - 1]] = left_counter

        elif left[index] == left[index + 1]:
            left_counter += 1

        elif left[index] != left[index + 1]:
            left_dict[left[index]] = left_counter
            left_counter = 1

    for index in range(len(right)):
        if index == len(right) - 1:
            if right[index] == right[index - 1]:
                right_dict[right[index]] = right_counter
            else:
                right_dict[right[index]] = right_counter
                right_dict[right[index - 1]] = right_counter

        elif right[index] == right[index + 1]:
            right_counter += 1

        elif right[index] != right[index + 1]:
            right_dict[right[index]] = right_counter
            right_counter = 1


    # print(left_dict)
    print(right)
    print(right_dict)

is_winning("Cash$$$$$$Ca$$$$$$sh")