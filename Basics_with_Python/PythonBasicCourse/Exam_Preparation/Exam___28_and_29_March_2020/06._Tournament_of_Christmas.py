winner = False
money_yearned = 0
win_count = 0
lose_count = 0
daily_earned = 0
daily_winner_counter = 0
daily_loser_counter = 0
earned = 0
total_earned = 0

days = int(input())
for _ in range(1, days + 1):

    while True:
        sport = input()
        if sport == "Finish":
            break
        result = input()
        if result == "win":
            earned += 20
            win_count += 1
        elif result == "lose":
            lose_count += 1

    if win_count > lose_count:
        daily_winner_counter += 1
        daily_earned += earned
        daily_earned *= 1.1
    else:
        daily_loser_counter += 1
        daily_earned += earned

    total_earned += daily_earned
    daily_earned = 0
    earned = 0
    win_count = 0
    lose_count = 0
if daily_winner_counter > daily_loser_counter:
    winner = True
    total_earned *= 1.2
if winner:
    print(f"You won the tournament! Total raised money: {total_earned:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_earned:.2f}")
