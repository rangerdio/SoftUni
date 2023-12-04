customers_qty = int(input())
product_count = 0
price = 0
bill = 0
average_current = 0
average = 0
for customer in range(1, customers_qty + 1):
    product_count = 0
    price = 0
    product = input()

    while product != "Finish":

        if product == "basket":
            price += 1.50
        elif product == "wreath":
            price += 3.8
        elif product == "chocolate bunny":
            price += 7
        product_count += 1
        product = input()

    if product_count % 2 == 0:
        price *= 0.80

    if product == "Finish":
        print(f"You purchased {product_count} items for {price:.2f} leva.")

    average += price

average = average / customers_qty
print(f"Average bill per client is: {average:.2f} leva.")
