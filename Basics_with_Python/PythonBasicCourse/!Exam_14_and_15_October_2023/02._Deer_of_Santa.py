import math
days_missing = int(input())
food_available = int(input())
deer1_daily_food = float(input())
deer2_daily_food = float(input())
deer3_daily_food = float(input())

total_needed_food = deer3_daily_food * days_missing + deer2_daily_food * days_missing + deer1_daily_food * days_missing
difference = abs(food_available - total_needed_food)
if food_available >= total_needed_food:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil((difference))} more kilos of food are needed.")
