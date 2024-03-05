items = {}
while True:
    command = input().split()
    if command[0] == "buy":
        break
    current_item, current_price, current_quantity = command[0], command[1], command[2]

    if current_item not in items.keys():
        items[current_item] = {"price": float(current_price), "quantity": int(current_quantity)}

    else:   # current_item exists
        if items[current_item]["price"] != float(current_price):
            items[current_item]["price"] = float(current_price)
        items[current_item]["quantity"] += int(current_quantity)


print(items)

for item in items:
    print(item)

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
