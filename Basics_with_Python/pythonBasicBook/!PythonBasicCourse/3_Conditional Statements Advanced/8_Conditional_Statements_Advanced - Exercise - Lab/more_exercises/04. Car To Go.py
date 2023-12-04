budged = float(input())
season = input()
car_class = 0
car = 0
car_price = 0

if budged <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        car_price = budged * 0.35
    elif season == "Winter":
        car = "Jeep"
        car_price = budged * 0.65

elif 100 < budged <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        car_price = budged * 0.45
    elif season == "Winter":
        car = "Jeep"
        car_price = budged * 0.80

elif budged > 500:
    car_class = "Luxury class"
    car = "Jeep"
    car_price = budged * 0.9

print(car_class)
print(f"{car} - {car_price:.2f}")
