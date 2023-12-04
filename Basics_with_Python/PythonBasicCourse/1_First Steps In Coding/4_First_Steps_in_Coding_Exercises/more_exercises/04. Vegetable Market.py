veg_price = float(input())
fruit_price = float(input())
veg_total = int(input())
fruit_total = int(input())
income = veg_total * veg_price + fruit_total * fruit_price
income_euro = income / 1.94
print(f"{income_euro:.2f}")
