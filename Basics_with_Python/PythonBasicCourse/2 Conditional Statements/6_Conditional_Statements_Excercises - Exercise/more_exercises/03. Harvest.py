import math
vineyard_area = int(input())
grapes_per_sqm_kg = float(input())
required_wine = int(input())
workers = int(input())

total_grape_production = vineyard_area * grapes_per_sqm_kg
grape_for_wine_kg = total_grape_production * 0.4
total_wine = grape_for_wine_kg / 2.5
ss = 0
if total_wine < required_wine:
    print(f"It will be a tough winter! More {int(math.floor(required_wine - total_wine))} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {int(math.floor(total_wine))} liters.")
    ss = (total_wine - required_wine) / workers
    print(f"{int(math.ceil(total_wine - required_wine))} liters left -> {int(math.ceil(ss))} liters per person.")
