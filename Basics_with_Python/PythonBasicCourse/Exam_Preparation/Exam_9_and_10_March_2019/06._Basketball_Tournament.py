win_counter = 0
lost_counter = 0
name = input()
while name != "End of tournaments":
    tournament_matches = int(input())
    for match_number in range(1, tournament_matches + 1):
        points_won = int(input())
        points_lost = int(input())
        difference = abs(points_lost - points_won)
        if points_won > points_lost:
            win_counter += 1
            print(f"Game {match_number} of tournament {name}: win with {difference} points.")
        else:
            lost_counter += 1
            print(f"Game {match_number} of tournament {name}: lost with {difference} points.")
    name = input()
total_matches = win_counter + lost_counter
wins = (win_counter / total_matches) * 100
lost = (lost_counter / total_matches) * 100
print(f"{wins:.2f}% matches win")
print(f"{lost:.2f}% matches lost")
