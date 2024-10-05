input_string = input()
cards_list = input_string.split()
team_a, team_b = [], []
terminated = False
for team_number in range(1, 12):
    team_a.append("A-" + str(team_number))
    team_b.append("B-" + str(team_number))

for current_card in cards_list:
    if current_card in team_a:
        team_a.remove(current_card)
    elif current_card in team_b:
        team_b.remove(current_card)
    if len(team_b) < 7 or len(team_a) < 7:
        terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if terminated:
    print("Game was terminated")
