fuel_type = input()
fuel = float(input())
card = input()
price = 0
if fuel_type == "Diesel":
    if card == "Yes":
        price = fuel * 2.33 - fuel * 0.12
    elif card == "No":
        price = fuel * 2.33

elif fuel_type == "Gasoline":
    if card == "Yes":
        price = fuel * 2.22 - fuel * 0.18
    elif card == "No":
        price = fuel * 2.22

elif fuel_type == "Gas":
    if card == "Yes":
        price = fuel * 0.93 - fuel * 0.08
    elif card == "No":
        price = fuel * 0.93
if fuel >= 20 and fuel <= 25:
    price = price * 0.92
elif fuel > 25:
    price = price * 0.9
print(f"{price:.2f} lv.")