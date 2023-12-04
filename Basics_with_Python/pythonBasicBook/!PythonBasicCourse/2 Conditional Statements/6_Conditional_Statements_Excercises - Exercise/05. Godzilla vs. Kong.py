budged = float(input())
extras = int(input())
extra_cloth_price = float(input())
decor = budged * 0.1
if extras > 150:
    extra_cloth_price = extra_cloth_price * 0.9
if decor + extras * extra_cloth_price > budged:
    print("Not enough money!")
    print(f"Wingard needs {(decor + extras * extra_cloth_price) - budged:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budged - (decor + extras * extra_cloth_price):.2f} leva left.")
