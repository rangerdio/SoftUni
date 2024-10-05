budged = float(input())
season = input()
destination = 0
money_to_spend = 0
hotel = 0

#select destination
if budged <= 100:
    destination = "Bulgaria"
elif budged > 100 and budged <= 1000:
    destination = "Balkans"
elif budged > 1000:
    destination = "Europe"

#define money to spend and the palce
if destination == "Bulgaria":
    if season == "summer":
        money_to_spend = budged * 0.3
        place = "Camp"
    elif season == "winter":
        money_to_spend = budged * 0.7
        place = "Hotel"
elif destination == "Balkans":
    if season == "summer":
        place = "Camp"
        money_to_spend = budged * 0.4
    elif season == "winter":
        place = "Hotel"
        money_to_spend = budged * 0.8
elif destination == "Europe":
        place = "Hotel"
        money_to_spend = budged * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {money_to_spend:.2f}")
