start_points = 301
player_name = input()
points_calc = 0
counter = 0
unsucc_counter = 0
area = input()
while area != "Retire":
    hit_points = int(input())
    if area == "Single":
        points_calc = hit_points
    elif area == "Double":
        points_calc = hit_points * 2
    elif area == "Triple":
        points_calc = hit_points * 3
    if points_calc > start_points:
        unsucc_counter += 1
        area = input()
        continue
    else:
        counter += 1
        start_points -= points_calc
    if start_points == 0:
        break  # win
    area = input()

if area == "Retire":
    print(f"{player_name} retired after {unsucc_counter} unsuccessful shots.")
elif start_points == 0:
    print(f"{player_name} won the leg with {counter} shots.")
