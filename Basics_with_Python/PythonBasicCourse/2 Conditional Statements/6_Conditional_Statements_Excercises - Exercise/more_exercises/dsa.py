import math
x = int(input())
y = float(input())
z = int(input())
number_of_workers = int(input())
wine_produced = x * y * 0.4 / 2.5

if wine_produced >= z:
    print(f"Good harvest this year! Total wine: {int(math.floor(wine_produced))} liters.")
    print(f"{int(math.ceil(wine_produced - z))} liters left -> {int(math.ceil(((wine_produced - z) / number_of_workers)))} liters per person.")
if wine_produced < z:
    print(f"It will be a tough winter! More {int(math.floor(z - wine_produced))} liters wine needed.")
