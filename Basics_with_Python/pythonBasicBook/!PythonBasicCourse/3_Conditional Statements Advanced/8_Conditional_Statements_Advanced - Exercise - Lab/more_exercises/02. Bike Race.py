juniors = int(input())
seniors = int(input())
race_type = input()
tax = 0
if race_type == "trail":
    tax = 5.50 * juniors + 7 * seniors
elif race_type == "cross-country":
    tax = 8 * juniors + 9.50 * seniors
elif race_type == "downhill":
    tax = 12.25 * juniors + 13.75 * seniors
elif race_type == "road":
    tax = 20 * juniors + 21.50 * seniors

if race_type == "cross-country" and seniors + juniors >= 50:
    tax = tax * 0.75
donation = tax * 0.95
print(f"{donation:.2f}")
