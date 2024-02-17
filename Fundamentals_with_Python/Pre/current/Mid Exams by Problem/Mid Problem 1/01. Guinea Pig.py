to_store = False


def daily_calculation(current_food: float, current_hay: float, current_cover: float, current_weight: float):
    return [current_food, current_hay, current_cover, current_weight]


food, hay_bought, cover, puppy_weight = float(input()), float(input()), float(input()), float(input())

for day in range(1, 31):
    current_day_result = daily_calculation(food, hay_bought, cover, puppy_weight)
    food, hay_bought, cover, puppy_weight = current_day_result[0], current_day_result[1], \
        current_day_result[2], current_day_result[3]
    if food <= 0 or hay_bought <= 0 or cover <= 0:
        to_store = True
        break
