fuel_type = input()
fuel_left = float(input())
fuel_type = fuel_type.lower()
if fuel_type == "diesel":
    if fuel_left >= 25:
        print(f"You have enough {fuel_type}.")
    else:
        print(f"Fill your tank with {fuel_type}!")
elif fuel_type == "gasoline":
    if fuel_left >= 25:
        print(f"You have enough {fuel_type}.")
    else:
        print(f"Fill your tank with {fuel_type}!")
elif fuel_type == "gas":
    if fuel_left >= 25:
        print(f"You have enough {fuel_type}.")
    else:
        print(f"Fill your tank with {fuel_type}!")
else:
    print("Invalid fuel!")