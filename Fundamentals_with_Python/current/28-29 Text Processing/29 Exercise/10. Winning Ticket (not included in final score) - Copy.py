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

            if best_match < 6:
                return ["no_match", best_match, best_match_symbol]
            else:   # >= 6, but not jackpot
                return ["winning", best_match, best_match_symbol]


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
