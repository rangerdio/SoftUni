season = input()
sex = input()
students = int(input())
nights = int(input())
price = 0
sport = 0
if sex == "boys":
    if season == "Winter":
        price = 9.60
        sport = "Judo"
    if season == "Spring":
        price = 7.20
        sport = "Tennis"
    if season == "Summer":
        price = 15
        sport = "Football"
elif sex == "girls":
    if season == "Winter":
        price = 9.60
        sport = "Gymnastics"
    if season == "Spring":
        price = 7.20
        sport = "Athletics"
    if season == "Summer":
        price = 15
        sport = "Volleyball"
elif sex == "mixed":
    if season == "Winter":
        price = 10
        sport = "Ski"
    if season == "Spring":
        price = 9.50
        sport = "Cycling"
    if season == "Summer":
        price = 20
        sport = "Swimming"


total = price * nights * students
if students >= 50:
    total = total * 0.50
elif 20 <= students < 50:
    total = total * 0.85
elif 10 <= students < 20:
    total = total * 0.95
print(f"{sport} {total:.2f} lv.")
