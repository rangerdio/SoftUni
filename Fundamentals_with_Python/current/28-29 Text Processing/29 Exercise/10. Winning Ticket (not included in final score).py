def isvalid(ticket):
    if len(ticket) == 20:
        return True
    else:
        return False


def is_winning(ticket):
    winner = False
    left = ticket[:10]
    right = ticket[10:]
    left_counter = 0
    right_counter = 0
    symbol = ""
    for index, letter in enumerate(left):
        if 10 > left.count(letter) >= 6:
            left_counter = left.count(letter)
            for letter_right in right:
                if 10 > right.count(letter) >= 6:
                    right_counter = right.count(letter)
                    symbol = letter
                    winner = True
    if winner:
        counter = left_counter if left_counter <= right_counter else right_counter
        print(f'ticket "{ticket}" - {counter}{symbol}')


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
             result = is_winning(element)



