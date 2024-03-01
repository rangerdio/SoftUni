products = {}

while True:
    product_list = input().split(": ")
    if product_list[0] == "statistics":
        break
    product_key = product_list[0]
    quantity = int(product_list[1])
    if product_key not in products:
        products[product_key] = 0
    products[product_key] += quantity

# for product, quant in products.items():
#     print(f"- {product}: {quant}")
print("Products in stock:")
[print(f"- {product}: {quant}") for product, quant in products.items()]

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
