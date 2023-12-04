budged = int(input())
season = input()
fishman = int(input())
rent_price = 0

if season == "Spring":
    rent_price = 3000
    if fishman <= 6:
        rent_price = rent_price * 0.90
    elif 7 <= fishman <= 11:
        rent_price = rent_price * 0.85
    elif fishman >= 12:
        rent_price = rent_price * 0.75

elif season == "Summer" or season == "Autumn":
    rent_price = 4200
    if fishman <= 6:
        rent_price = rent_price * 0.90
    elif 7 <= fishman <= 11:
        rent_price = rent_price * 0.85
    elif fishman >= 12:
        rent_price = rent_price * 0.75

elif season == "Winter":
    rent_price = 2600
    if fishman <= 6:
        rent_price = rent_price * 0.90
    elif 7 <= fishman <= 11:
        rent_price = rent_price * 0.85
    elif fishman >= 12:
        rent_price = rent_price * 0.75


if (fishman % 2 == 0) and (season == "Spring" or season == "Summer" or season == "Winter"):
    rent_price == rent_price * 0.95

difference = abs(budged - rent_price)

if budged >= rent_price:
    print(f"Yes! You have {difference:.2f} leva left.")
elif budged < rent_price:
    print(f"Not enough money! You need {difference:.2f} leva.")
