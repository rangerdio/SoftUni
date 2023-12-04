import math
days = int(input())
food_kg = int(input())
dog_daily_needs = float(input())
cat_daily_needs = float(input())
turt_daily_gr_needs = float(input())
turt_daily_needs = turt_daily_gr_needs / 1000
dog_daily_needs = dog_daily_needs * days
cat_daily_needs = cat_daily_needs * days
turt_daily_needs = turt_daily_needs * days
total_daily_needs = dog_daily_needs + cat_daily_needs + turt_daily_needs
difference = abs(total_daily_needs - food_kg)

if food_kg > total_daily_needs:
    print(f"{int(difference)} kilos of food left.")
else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")
