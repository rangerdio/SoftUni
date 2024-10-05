drink = input()
sugar = input()
quantity = int(input())
price = 0
if drink == "Espresso":
    if sugar == "Without":
        price = 0.90
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.60
elif drink == "Tea":
    if sugar == "Without":
        price = 0.5
    elif sugar == "Normal":
        price = 0.6
    elif sugar == "Extra":
        price = 0.7

bill = quantity * price
if sugar == "Without":
    #  bill = bill - bill * 35 / 100
    bill = bill * 0.65
if drink == "Espresso" and quantity >=  5:
    #  bill = bill - bill * 25 / 100
    bill = bill * 0.75
if bill > 15:
    bill = bill * 0.80

print(f"You bought {quantity} cups of {drink} for {bill:.2f} lv.")