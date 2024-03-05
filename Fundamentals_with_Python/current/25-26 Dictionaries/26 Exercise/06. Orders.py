items = {}
while True:
    command = input().split()
    if command[0] == "buy":
        break
    current_item, current_price, current_quantity = command[0], command[1], command[2]

    if current_item not in items:
        items[current_item] = {float(current_price): int(current_quantity)}

    else:   # current_item exists
        for key, value in items[current_item].items():
            items[current_item] = current_price
            items[current_item][key] += int(current_quantity)
print(items)


# items = {}
# while True:
#     command = input().split()
#     if command[0] == "buy":
#         break
#     current_item, current_price, current_quantity = command[0], command[1], command[2]
#
#     if current_item not in items:
#         items[current_item] = {float(current_price): int(current_quantity)}
#
#     else:   # current_item exists
#         for key, value in items[current_item].items():
#             items[current_item] = current_price
#             items[current_item][key] += int(current_quantity)
#
# print(items)
#
# # for element in current_items:
# #     for key in element.keys():
# #         print(f"{key} -> {element[key]:.2f}")
