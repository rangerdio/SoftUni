def analyse(ticket: str):
    left_side = ticket[0:10]
    right_side = ticket[10:]
    if "@" or "#" or "$" or "^" in ticket:  # winning ticket
        if left_side == right_side:         # jackpot
            return ["jackpot", len(left_side), left_side[0]]
        else:   # winning : 6-9 matches or not winning : 1-5 matches
            best_match = 0
            count_match = 1
            best_match_symbol = ""
            previous_state = False

            for index in range(len(ticket)):
                if index == len(ticket) - 1:
                    continue

                if ticket[index] == ticket[index + 1]:
                    count_match += 1

                #    previous_state = True
                elif ticket[index] != ticket[index + 1]:
                    if count_match > best_match:
                        best_match = count_match
                        count_match = 1
                        best_match_symbol = ticket[index]
                    else:
                        count_match = 1
