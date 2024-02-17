def daily_calculation(current_food: float, current_hay: float, current_cover: float, current_weight: float, day_):
    current_food -= 0.300
    if day_ % 2 == 0:
        current_hay -= 5 * current_food / 100
    if day_ % 3 == 0:
        current_cover -= current_weight / 3
    return [current_food, current_hay, current_cover]


to_store = False
food, hay_bought, cover, puppy_weight = float(input()), float(input()), float(input()), float(input())

for day in range(1, 31):
    current_day_result = daily_calculation(food, hay_bought, cover, puppy_weight, day)
    food, hay_bought, cover, puppy_weight = current_day_result[0], current_day_result[1], \
        current_day_result[2], current_day_result[3]
    if food <= 0 or hay_bought <= 0 or cover <= 0:
        to_store = True
        break

if to_store:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food}, Hay: {hay_bought}, Cover: {cover}.")
