winner_symbols = ["@", "#", "$", "^"]
valid_len = 20
tickets = [ticket_.strip() for ticket_ in input().split(",")]
# tickets = [ticket_.strip() for ticket_ in "validticketnomatch:(, Cas$$$$$$$Ca$$$$$$s$".split(",")]

for ticket in tickets:
    if len(ticket) != valid_len:
        print("invalid ticket")
        continue
    else:  # ticket_ is valid
        left_side = ticket[0:10]
        right_side = ticket[10:]
        found_winner = False

        for symbol in winner_symbols:
            if symbol * 20 == ticket:
                print(f'ticket "{ticket}" - {10}{symbol} Jackpot!')
                found_winner = True
                break
            elif symbol * 9 in left_side and symbol * 9 in right_side:
                print(f'ticket "{ticket}" - {9}{symbol}')
                found_winner = True
                break
            elif symbol * 8 in left_side and symbol * 8 in right_side:
                print(f'ticket "{ticket}" - {8}{symbol}')
                found_winner = True
                break
            elif symbol * 7 in left_side and symbol * 7 in right_side:
                print(f'ticket "{ticket}" - {7}{symbol}')
                found_winner = True
                break
            elif symbol * 6 in left_side and symbol * 6 in right_side:
                print(f'ticket "{ticket}" - {6}{symbol}')
                found_winner = True
                break
        if not found_winner:
            print(f'ticket "{ticket}" - no match')