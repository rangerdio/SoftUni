qty = int(input())
days_left = int(input())
budged = 0
total_spirit = 0
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

for day in range(1, days_left + 1):
    if day % 11 == 0:
        qty += 2
    if day % 2 == 0:
        budged += qty * ornament_set_price
        total_spirit += 5
    if day % 3 == 0:
        budged += qty * (tree_skirt_price + tree_garland_price)
        total_spirit += 3 + 10
    if day % 5 == 0:
        budged += qty * tree_lights_price
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        budged += tree_skirt_price + tree_garland_price + tree_lights_price

if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budged}")
print(f"Total spirit: {total_spirit}")


#
# qty = int(input())
# days_left = int(input())
# budged = 0
# total_spirit = 0
# ornament_set = 0
# tree_skirt = 0
# tree_garland = 0
# tree_lights = 0
# points = 0
# price_piece = 0
# day = 0
# ornament_set_price = 2
# tree_skirt_price = 5
# tree_garland_price = 3
# tree_lights_price = 15
# multiplier = 0
#
# for day in range(1, days_left + 1):
#
#     if day % 11 == 0:
#         multiplier += 2
#     if day % 2 == 0:
#         ornament_set += qty + multiplier
#         points += 5
#     if day % 3 == 0:
#         tree_skirt += qty + multiplier
#         points += 3
#         tree_garland += qty + multiplier
#         points += 10
#     if day % 5 == 0:
#         tree_lights += qty + multiplier
#         points += 17
#         if day % 3 == 0:
#             points += 30
#     if day % 10 == 0:
#         points -= 20
#         tree_skirt += 1
#         tree_garland += 1
#         tree_lights += 1
#
# if days_left % 10 == 0:
#     points -= 30
#
# budged = ornament_set * ornament_set_price + tree_skirt * tree_skirt_price +\
#          tree_garland * tree_garland_price + tree_lights * tree_lights_price
#
# print(f"Total cost: {budged}")
# print(f"Total spirit: {points}")
