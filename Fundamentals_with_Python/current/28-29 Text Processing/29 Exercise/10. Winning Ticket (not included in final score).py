def isvalid(ticket):
    if len(ticket) == 20:
        return True
    else:
        return False


def confirm_winner(left_d: dict, right_d: dict, ticket__):
    left_symbol = ""
    right_symbol = ""
    left_symbol_value = ""
    right_symbol_value = ""

    for key, value in left_d.items():
        if value >= 6:
            left_symbol = key
            left_symbol_value = left_d[left_symbol]

    for key, value in right_d.items():
        if value >= 6:
            right_symbol = key
            right_symbol_value = right_d[right_symbol]
    # print(right_symbol_value)

    if left_symbol and right_symbol:
        if left_symbol != right_symbol:
            print(f'"ticket "{ticket__}" - no match')
        else:
            symbol = right_symbol if left_symbol_value > right_symbol_value else left_symbol
            print(f'ticket "{ticket__}" - {right_symbol_value}{symbol}')

    elif not left_symbol or not right_symbol:
        print(f'"ticket "{element}" - no match')


def is_winning(ticket):
    left = ticket[:10]
    right = ticket[10:]

    left_counter = 1
    right_counter = 1

    left_dict = {}
    right_dict = {}

    for index in range(len(left)):
        if index == len(left) - 1:
            left_dict[left[index]] = max(left_counter, left_dict.get(left[index], 0))
        elif left[index] == left[index + 1]:
            left_counter += 1
        else:
            left_dict[left[index]] = max(left_counter, left_dict.get(left[index], 0))
            left_counter = 1

    for index in range(len(right)):
        if index == len(right) - 1:
            right_dict[right[index]] = max(right_counter, right_dict.get(right[index], 0))
        elif right[index] == right[index + 1]:
            right_counter += 1
        else:
            right_dict[right[index]] = max(right_counter, right_dict.get(right[index], 0))
            right_counter = 1

    # print(left_dict)
    # print(right)
    # print(right_dict)
    confirm_winner(left_dict, right_dict, ticket)


line = input()
tickets = line.split()
tickets = "".join(tickets)
tickets = tickets.split(",")

for element in tickets:
    if not isvalid(element):
        print("invalid ticket")
    else:
        if element[:10] == element[10:]:
            print(f'ticket "{element}" - {10}{element[0]} Jackpot!')

        elif element[:10] != element[10:]:
            is_winning(element)
