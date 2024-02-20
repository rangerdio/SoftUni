order_qty = int(input())
total_price = 0

for order in range(order_qty):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if (not 100.00 >= price_per_capsule >= 0.01) or (not 31 >= days >= 1) or (not 2000 >= capsules_per_day >= 1):
        continue
    price = days * capsules_per_day * price_per_capsule
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price
    price = 0
print(f"Total: ${total_price:.2f}")
