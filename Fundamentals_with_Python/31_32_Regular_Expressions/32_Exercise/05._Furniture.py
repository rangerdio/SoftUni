import re
items = []
total_cost = 0


while True:
    current_item = input()
    if current_item == "Purchase":
        break
    pattern = r'^>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)$'
    matches = re.findall(pattern, current_item)
    if matches:
        for match in matches:
            furniture_name, price, quantity = match[0], float(match[1]), int(match[2])
            total_cost += price * quantity
            items.append(furniture_name)


print("Bought furniture:")
for item in items:
    print(item)
print(f'Total money spend: {total_cost:.2f}')
