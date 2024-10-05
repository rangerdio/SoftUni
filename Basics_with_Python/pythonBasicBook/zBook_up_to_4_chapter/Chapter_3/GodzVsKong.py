budged = float(input())
extras = int(input())
clots = float(input())

decor_budged = 0.1 * budged
needed = 0
if extras > 150:
    clots = clots * 0.9 * extras
    needed = decor_budged + clots
    if needed > budged:
        print("Not enough money!")
        print(f"Wingard needs {(abs(budged - needed)):.2f} leva more.")
    else:
        print("Action!")
        print(f"Wingard starts filming with {(abs(budged - needed)):.2f} leva left.")
else:
    clots = clots * extras
    needed = decor_budged + clots
    if needed > budged:
        print("Not enough money!")
        print(f"Wingard needs {(abs(budged - needed)):.2f} leva more.")
    else:
        print("Action!")
        print(f"Wingard starts filming with {(abs(budged - needed)):.2f} leva left.")
