chicken = int(input())
fish = int(input())
vegetarian = int(input())

total_food = chicken * 10.35 + fish * 12.40 + vegetarian * 8.15
total_food_with_sweets = total_food * 1.2
with_delivery = total_food_with_sweets + 2.5
print(with_delivery)
