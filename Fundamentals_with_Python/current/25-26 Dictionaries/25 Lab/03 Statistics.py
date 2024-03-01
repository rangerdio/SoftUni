products = {}

while True:
    product_list = input().split(": ")
    if product_list[0] == "statistics":
        break
    product_key = product_list[0]
    quantity = int(product_list[1])
    if product_key not in products:
        products[product_key] = quantity
    products[product_key] += quantity

print(products)
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
