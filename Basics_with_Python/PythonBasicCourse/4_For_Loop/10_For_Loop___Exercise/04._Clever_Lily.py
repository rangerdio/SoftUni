n = int(input())
washer_price = float(input())
toy_price = float(input())
toy_count = 0
money_presents = 0
addition = 10
for number in range(1, n + 1):
    if number % 2 == 0:
        money_presents += addition - 1
        addition += 10
    else:
        toy_count += 1
toy_money = toy_count * toy_price
saves = toy_money + money_presents
if saves >= washer_price:
    print(f"Yes! {abs(washer_price - saves):.2f}")
else:
    print(f"No! {abs(washer_price - saves):.2f}")
