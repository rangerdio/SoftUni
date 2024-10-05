import math
racquet_price = float(input())
racquet_qty = int(input())
boots_qty = int(input())
boots_price = racquet_price / 6
items = racquet_qty * racquet_price + boots_price * boots_qty
others = items * 0.20
total = items + others
pay_me = total / 8
pay_sponsors = 7 * total / 8
print(f"Price to be paid by Djokovic {math.floor(pay_me)}")
print(f"Price to be paid by sponsors {math.ceil(pay_sponsors)}")
