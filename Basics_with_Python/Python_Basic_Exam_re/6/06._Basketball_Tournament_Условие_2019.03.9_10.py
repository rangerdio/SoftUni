tournament_name = input()
match_count = 0
total_count = 0
win_count = 0
lose_count = 0
wins = 0
loses = 0
while tournament_name != "End of tournaments":
    match_qty = int(input())
    match_count = 0
    for m in range(1, match_qty + 1):
        match_points_desi = int(input())
        match_points_opponent = int(input())
        match_count += 1
        total_count += 1
        diff = abs(match_points_desi - match_points_opponent)
        if match_points_desi > match_points_opponent:
            win_count += 1
            print(f"Game {match_count} of tournament {tournament_name}: win with {diff} points.")
        elif match_points_desi < match_points_opponent:
            lose_count += 1
            print(f"Game {match_count} of tournament {tournament_name}: lost with {diff} points.")
    tournament_name = input()
wins = 100 * win_count / total_count
loses = 100 * lose_count / total_count

if tournament_name == "End of tournaments":
    print(f"{wins:.2f}% matches win")
    print(f"{loses:.2f}% matches lost")
