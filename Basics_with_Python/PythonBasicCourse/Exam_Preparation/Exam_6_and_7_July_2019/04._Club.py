profit = float(input())
income = 0
deal = 0
cocktail_name = input()
while True:
    if cocktail_name == "Party!":
        break
    quantity = int(input())
    price = len(cocktail_name)
    deal = quantity * price
    if deal % 2 != 0:
        deal *= 0.75
    income += deal
    if income >= profit:
        break
    cocktail_name = input()
    if cocktail_name == "Party!":
        break


if profit > income:
    print(f"We need {abs(profit - income):.2f} leva more.")
    print(f"Club income - {income:.2f} leva.")
else:
    print(f"Target acquired.")
    print(f"Club income - {income:.2f} leva.")
