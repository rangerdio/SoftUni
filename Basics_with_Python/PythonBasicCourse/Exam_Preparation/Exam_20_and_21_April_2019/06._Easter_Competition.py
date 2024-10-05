cake_competitors = int(input())
competitor_points = 0
competitor_count = 0
next_competitor = False
winner_points = 0
winner_name = ""

chef_name = input()
while chef_name != "Stop":
    competitor_count += 1

    while True:
        result = input()
        if result == "Stop":
            next_competitor = True
            break
        result = int(result)
        competitor_points += result
    print(f"{chef_name} has {competitor_points} points.")
    if competitor_points > winner_points:
        winner_points = competitor_points
        winner_name = chef_name
        print(f"{winner_name} is the new number 1!")
    competitor_points = 0
    if competitor_count == cake_competitors:
        break
    elif competitor_count < cake_competitors:
        chef_name = input()
        if chef_name == "Stop":
            break
print(f"{winner_name} won competition with {winner_points} points!")
