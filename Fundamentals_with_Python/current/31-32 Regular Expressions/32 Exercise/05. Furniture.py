import re
items = []
total_cost = 0


while True:
    current_item = input()
    if current_item == "Purchase":
        break
    pattern = r''
    # furniture_name, price, quantity = re.finditer(pattern, current_item)
    furniture_name = re.findall(r'((?<=>>)[A-Za-z]+)(?=<<)', current_item)
    price = re.findall(r'(?<=<<)\d+\.?\d*(?=!)', current_item)
    quantity = re.findall(r'(?<=!)\d+$', current_item)
    # print(furniture_name, price, quantity)
    if furniture_name and price and quantity:
        price, quantity, furniture_name = float(price[0]), int(quantity[0]), furniture_name[0]
        total_cost += price * quantity
        items.append(furniture_name)

print("Bought furniture:")
for item in items:
    print(item)
print(f'Total money spend: {total_cost}')
