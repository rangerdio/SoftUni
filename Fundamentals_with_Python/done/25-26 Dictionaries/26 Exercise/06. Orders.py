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

for item in items.keys():
    items[item] = items[item]["price"] * items[item]["quantity"]

for item in items.keys():
    print(f"{item} -> {items[item]:.2f}")