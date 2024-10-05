best_player_goals = 0
is_found = False
is_middle = False

player_name = input()
best_player_name = player_name

while player_name != "END":
    goals = int(input())
    is_middle = False
    if goals >= 10:
        best_player_goals = goals
        best_player_name = player_name
        break
    elif goals > best_player_goals:
        best_player_goals = goals
        best_player_name = player_name
        is_middle = True
    player_name = input()

print(f"{best_player_name} is the best player!")
if best_player_goals >= 3:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")
