types = input()
rows = int(input())
cols = int(input())
price = 0
if types == "Premiere":
    price = 12.00
elif types == "Normal":
    price = 7.50
elif types == "Discount":
    price = 5.00
total = rows * cols * price
print(f"{total:.2f} leva")
