fruit_type = input()
size = input()
set_qty_ordered = int(input())
seal_price = 0
set_qty_seals = 0
discount = 1

if size == "small":
    set_qty_seals = 2
    if fruit_type == "Watermelon":
        seal_price = 56
    elif fruit_type == "Mango":
        seal_price = 36.66
    elif fruit_type == "Pineapple":
        seal_price = 42.10
    elif fruit_type == "Raspberry":
        seal_price = 20


elif size == "big":
    set_qty_seals = 5
    if fruit_type == "Watermelon":
        seal_price = 28.70
    elif fruit_type == "Mango":
        seal_price = 19.60
    elif fruit_type == "Pineapple":
        seal_price = 24.80
    elif fruit_type == "Raspberry":
        seal_price = 15.20

set_price = seal_price * set_qty_seals
total = set_price * set_qty_ordered

if (total >= 400) and (total <= 1000):
    discount = 0.85
elif total > 1000:
    discount = 0.50
else:
    discount = 1
after_discount = total * discount

print(f"{after_discount:.2f} lv.")
