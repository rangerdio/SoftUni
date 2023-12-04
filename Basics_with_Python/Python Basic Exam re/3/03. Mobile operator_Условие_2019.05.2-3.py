length = input()
plan = input()
mobile_Net = input()
months_Qty = int(input())
monthly_tax = 0
discount = 0

if length == "one":
    discount = 1
    if plan == "Small":
        monthly_tax = 9.98
    elif plan == "Middle":
        monthly_tax = 18.99
    elif plan == "Large":
        monthly_tax = 25.98
    elif plan == "ExtraLarge":
        monthly_tax = 35.99

elif length == "two":
    discount = (100 - 3.75) / 100
    if plan == "Small":
        monthly_tax = 8.58
    elif plan == "Middle":
        monthly_tax = 17.09
    elif plan == "Large":
        monthly_tax = 23.59
    elif plan == "ExtraLarge":
        monthly_tax = 31.79

if mobile_Net == "yes":
    if monthly_tax <= 10:
        monthly_tax += 5.50
    elif (monthly_tax > 10) and (monthly_tax <= 30):
        monthly_tax += 4.35
    elif monthly_tax > 30:
        monthly_tax += 3.85

total = months_Qty * monthly_tax * discount
print(f"{total:.2f} lv.")
