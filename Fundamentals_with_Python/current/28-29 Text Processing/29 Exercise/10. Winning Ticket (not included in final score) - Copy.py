def analyse(ticket_: str):

    return asd


# tickets = [ticket.strip() for ticket in input().split(",")]
tickets = [ticket.strip() for ticket in "$$$$$$$$$$$$$$$$$$$$, aabb  , th@@@@@@eemo@@@@@@ey".split(",")]

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
    else:  # ticket is valid
        if analyse(ticket)[0] == "jackpot":
            print(f"ticket {ticket} - {analyse(ticket)[1]}{analyse(ticket)[2]} Jackpot!")
        elif analyse(ticket)[0] == "winning":
            print(f"ticket {ticket} - {analyse(ticket)[1]}{analyse(ticket)[2]}")
        elif analyse(ticket)[0] == "no_match":
            print(f"ticket {ticket} - no match")
