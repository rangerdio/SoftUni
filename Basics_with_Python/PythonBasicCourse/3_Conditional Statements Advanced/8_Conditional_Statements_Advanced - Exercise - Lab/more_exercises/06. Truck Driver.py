season = input()
km_monthly = float(input())
km_price = 0
if km_monthly <= 5000:
    if season == "Spring" or season == "Autumn":
        km_price = 0.75
    elif season == "Summer":
        km_price = 0.90
    elif season == "Winter":
        km_price = 1.05
elif 5000 < km_monthly <= 10000:
    if season == "Spring" or season == "Autumn":
        km_price = 0.95
    elif season == "Summer":
        km_price = 1.10
    elif season == "Winter":
        km_price = 1.25
elif 10000 < km_monthly <= 20000:
    if season == "Spring" or season == "Autumn" or season == "Summer" or season == "Winter":
        km_price = 1.45
print(f"{(km_price * km_monthly * 4 * 0.9):.2f}")
