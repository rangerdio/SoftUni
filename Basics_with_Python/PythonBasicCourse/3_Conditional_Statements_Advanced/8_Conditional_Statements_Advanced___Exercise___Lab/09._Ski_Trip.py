days = int(input())
type_room = input()
rating = input()
price = 0
days = days - 1 #nights
if type_room == "room for one person":
        price = 18 * days
elif type_room == "apartment":
    if days < 10:
        price = 25 * days * 0.70
    elif days >= 10 and days <= 15:
        price = 25 * days * 0.65
    elif days > 15:
        price = 25 * days * 0.50
elif type_room == "president apartment":
    if days < 10:
        price = 35 * days * 0.9
    elif days >= 10 and days < 15:
        price = 35 * days * 0.85
    elif days > 15:
        price = 35 * days * 0.80
if rating == "positive":
    price = price * 1.25
else:
    price = price * 0.90
print(f"{price:.2f}")
