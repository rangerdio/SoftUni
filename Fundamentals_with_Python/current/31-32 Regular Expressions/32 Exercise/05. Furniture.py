import re
items = []
total_cost = 0

current_item = input()
while current_item != "Purchase":
    pattern = r''
    furniture_name, price, quantity = re.finditer(pattern, current_item)
    total_cost += price * quantity
    items.append(total_cost)

print("Bought furniture:")
for item in items:
    print(item)
print(f'Total money spend: {total_cost}')
