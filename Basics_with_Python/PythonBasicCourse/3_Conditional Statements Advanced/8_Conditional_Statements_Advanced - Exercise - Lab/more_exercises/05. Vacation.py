budged = float(input())
season = input()
price = 0
place = 0
location =0

if budged <= 1000:
    place = "Camp"
    if season == "Summer":
        price = budged * 0.65
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"
        price = budged * 0.45
elif 1000 < budged <=3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budged * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budged * 0.60

elif budged > 3000:
    place = "Hotel"
    price = budged * 0.9
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"
print(f"{location} - {place} - {price:.2f}")
