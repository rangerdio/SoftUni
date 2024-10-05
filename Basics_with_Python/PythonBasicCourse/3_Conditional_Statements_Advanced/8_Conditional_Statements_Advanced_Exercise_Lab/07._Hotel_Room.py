month = input()
nights = int(input())
studio = 0
app = 0

if month == "May" or month == "October":
    studio = 50
    app = 65
    if nights > 7 and nights <= 14:
        studio = studio * 0.95
    elif nights > 14:
        studio = studio * 0.7
        app = app * 0.9

elif month == "June" or month == "September":
    studio = 75.2
    app = 68.70
    if nights > 14:
        studio = studio * 0.8
        app = app * 0.9

elif month == "July" or month == "August":
    studio = 76
    app = 77
    if nights > 14:
        app = app * 0.9
studio_total = studio * nights
app_total = app * nights
print(f"Apartment: {app_total:.2f} lv.")
print(f"Studio: {studio_total:.2f} lv.")
