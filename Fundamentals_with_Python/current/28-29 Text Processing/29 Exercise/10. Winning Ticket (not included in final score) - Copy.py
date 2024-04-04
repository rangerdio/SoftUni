def analyse(ticket: str):
    left_side = ticket[0:10]
    right_side = ticket[10:]
    if "@" or "#" or "$" or "^" in ticket:
        if left_side == right_side:
            return ["jackpot", len(left_side), left_side[0]]
        else:
            return [1,2,3]


# ticket_s = [ticket_.strip() for ticket_ in input().split(",")]
ticket_s = [ticket_.strip() for ticket_ in "$$$$$$$$$$$$$$$$$$$$, aabb  , th@@@@@@eemo@@@@@@ey".split(",")]

for ticket_ in ticket_s:
    if len(ticket_) != 20:
        print("invalid ticket_")
    else:  # ticket_ is valid
        analyse_ticket = analyse(ticket_)
        # print(analyse_ticket)

        if analyse_ticket[0] == "jackpot":
            print(f"ticket {ticket_} - {analyse_ticket[1]} {analyse_ticket[2]} Jackpot!")
        elif analyse_ticket[0] == "winning":
            print(f"ticket {ticket_} - {analyse_ticket[1]}{analyse_ticket[2]}")
        elif analyse(ticket_)[0] == "no_match":
            print(f"ticket {ticket_} - no match")
