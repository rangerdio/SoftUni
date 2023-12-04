budged = float(input())
sex = input()
age = int(input())
sport = input()
card = 0

if sex == "m":
    if sport == "Gym":
        card = 42
    elif sport == "Boxing":
        card = 41
    elif sport == "Yoga":
        card = 45
    elif sport == "Zumba":
        card = 34
    elif sport == "Dances":
        card = 51
    elif sport == "Pilates":
        card = 39

elif sex == "f":
    if sport == "Gym":
        card = 35
    elif sport == "Boxing":
        card = 37
    elif sport == "Yoga":
        card = 42
    elif sport == "Zumba":
        card = 31
    elif sport == "Dances":
        card = 53
    elif sport == "Pilates":
        card = 37

if age <= 19:
    card *= 0.80
diff = abs(budged - card)
if card <= budged:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${diff:.2f} more.")
