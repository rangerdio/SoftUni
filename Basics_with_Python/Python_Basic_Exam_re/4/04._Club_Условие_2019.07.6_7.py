req_profit = float(input())
cocktail_price = 0
cocktail_name = input()
order_price = 0
real_profit = 0
is_target_reached = False

while cocktail_name != "Party!":
    cocktail_price = len(cocktail_name)
    cocktail_qty = int(input())
    order_price = cocktail_price * cocktail_qty

    if order_price % 2 != 0:
        order_price *= 0.75

    real_profit += order_price
    if real_profit >= req_profit:
        is_target_reached = True
        break
    cocktail_name = input()

diff = abs(real_profit - req_profit)

if cocktail_name == "Party!":
    print(f"We need {diff:.2f} leva more.")
elif is_target_reached:
    print("Target acquired.")
print(f"Club income - {real_profit:.2f} leva.")
