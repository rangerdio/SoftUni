flag1 = False
team_name = input()
matches = int(input())
wins = 0
draws = 0
loses = 0
points = 0
for num in range(1, matches + 1):
    if matches == 0:
        break
    result = input()
    if result == "W":
        wins += 1
        points += 3
    elif result == "D":
        draws += 1
        points += 1
    elif result == "L":
        loses += 1
        continue

if matches == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    win1 = wins * 100 / matches
    print(f"{team_name} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {win1:.2f}%")
