products = {}
while True:
    line = input()
    if line == "statistics":
        break
    line = line.split(": ")
    if line[0] in products:
        products[line[0]] += int(line[1])
    else:
        products[line[0]] = int(line[1])

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")

