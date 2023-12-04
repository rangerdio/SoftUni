budged = float(input())
spend = 0
counter = 0
product_name = input()
future_counter = 0

while product_name != "Stop":
    product_price = float(input())
    future_counter += 1
    if future_counter % 3 == 0:
        product_price /= 2
    spend += product_price
    if spend > budged:
        break
    counter += 1
    product_name = input()

diff = abs(spend - budged)

if product_name == "Stop":
    print(f"You bought {counter} products for {spend:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {diff:.2f} leva!")
