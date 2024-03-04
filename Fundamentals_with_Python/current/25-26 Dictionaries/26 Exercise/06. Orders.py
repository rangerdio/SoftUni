items = {}
while True:
    command = input().split()
    if command[0] == "buy":
        break
    current_item, current_price, current_quantity = command[0], command[1], command[2]

    if current_item not in items:
        items[current_item] = {float(current_price): int(current_quantity)}
    
    else:   # current_item exists
        inside_dictionary = items[current_item]
        for key, value in inside_dictionary.items():
            inside_dictionary[key] += current_quantity





print(items)

# for element in current_items:
#     for key in element.keys():
#         print(f"{key} -> {element[key]:.2f}")
