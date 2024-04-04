def analyse(ticket: str):
    left_side = ticket[0:10]
    right_side = ticket[10:]
    if "@" or "#" or "$" or "^" in ticket:  # winning ticket
        if left_side == right_side:         # jackpot
            return ["jackpot", len(left_side), left_side[0]]
        else:   # winning : 6-9 matches or not winning : 1-5 matches
            best_match = 0
            count_match = 1
            best_match_right = 0
            count_match_right = 1
            best_match_symbol = ""
            best_match_symbol_right = ""

            for index in range(len(left_side)):
                if index == len(left_side) - 1:
                    if count_match > best_match:
                        best_match = count_match
                        count_match = 1
                        best_match_symbol = left_side[index]
                    else:
                        count_match = 1
                    continue

                if left_side[index] == left_side[index + 1]:
                    count_match += 1

                #    previous_state = True
                elif left_side[index] != left_side[index + 1]:
                    if count_match > best_match:
                        best_match = count_match
                        count_match = 1
                        best_match_symbol = left_side[index]
                    else:
                        count_match = 1

            if best_match < 6 and best_match_symbol in win_syms:  # no need to check right side
                return ["no_match", best_match, best_match_symbol]

            else:   # do the same check for right side, and verify if best match symbol is same >= 6, but not jackpot
                for index in range(len(right_side)):
                    if index == len(right_side) - 1:
                        if count_match_right > best_match_right:
                            best_match_right = count_match_right
                            count_match_right = 1
                            best_match_symbol_right = right_side[index]
                        else:
                            count_match_right = 1
                        continue

                    if right_side[index] == right_side[index + 1]:
                        count_match_right += 1

                    elif right_side[index] != right_side[index + 1]:
                        if count_match_right > best_match_right:
                            best_match_right = count_match_right
                            count_match_right = 1
                            best_match_symbol_right = right_side[index]
                        else:
                            count_match_right = 1

                if best_match_right >= 6 and best_match_symbol_right == best_match_symbol and best_match_symbol in win_syms:  # no need to check right side
                    return ["winning", best_match_right, best_match_symbol_right]


win_syms = ["@", "#", "$", "^"]
ticket_s = [ticket_.strip() for ticket_ in input().split(",")]
# ticket_s = [ticket_.strip() for ticket_ in "validticketnomatch:(, Cas$$$$$$$Ca$$$$$$s$".split(",")]

for ticket_ in ticket_s:
    if len(ticket_) != 20:
        print("invalid ticket")
    else:  # ticket_ is valid
        analyse_ticket = analyse(ticket_)
        # print(analyse_ticket)

        if analyse_ticket[0] == "jackpot":
            print(f'ticket "{ticket_}" - {analyse_ticket[1]}{analyse_ticket[2]} Jackpot!')
        elif analyse_ticket[0] == "winning":
            print(f'ticket "{ticket_}" - {analyse_ticket[1]}{analyse_ticket[2]}')
        elif analyse(ticket_)[0] == "no_match":
            print(f'ticket "{ticket_}" - no match')
