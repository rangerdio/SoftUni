days = int(input())
total_income = 0
day_winner = 0

for day in range(1, days + 1):
    win_cnt = 0
    lost_cnt = 0
    income = 0
    sport = input()
    while sport != "Finish":

        result = input()
        if result == "win":
            income += 20
            win_cnt += 1
        else:
            lost_cnt += 1
        sport = input()

    if win_cnt > lost_cnt:
        income *= 1.1
        day_winner += 1
    total_income += income
if day_winner > days / 2:
    total_income *= 1.2
    print(f"You won the tournament! Total raised money: {total_income:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_income:.2f}")
