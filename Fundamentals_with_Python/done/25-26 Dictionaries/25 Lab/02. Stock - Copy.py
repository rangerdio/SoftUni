line = input().split(" ")
search = input().split()
stock = {}
for index in range(0, len(line), 2):
    stock[line[index]] = int(line[index + 1])
for product in search:
    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
