price_dict = {}
qty_dict = {}


while True:
    line = input().split()
    if line == "buy":
        break
    product, price, qty = line[0], float(line[1]), int(line[2])

    if product not in price_dict.keys():
        price_dict[product] = price
        qty_dict[product] = qty
    else:
        price_dict[product] = price
        qty_dict[product] += qty

for