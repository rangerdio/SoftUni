discount = False
purchase_counter = 0
clients = int(input())
bill = 0
price = 0
counter_keeper = 0
total_bills = 0

for client in range(1, clients + 1):
    purchase_counter = 0
    bill = 0
    purchase = input()
    while purchase != "Finish":
        discount = False
        purchase_counter += 1
        if purchase == "basket":
            price = 1.5
        elif purchase == "wreath":
            price = 3.8
        elif purchase == "chocolate bunny":
            price = 7
        bill += price
        counter_keeper = purchase_counter
        if counter_keeper % 2 == 0:
            discount = True
        purchase = input()
    if discount:
        bill *= 0.8
    total_bills += bill
    print(f"You purchased {counter_keeper} items for {bill:.2f} leva.")
average = total_bills / clients
print(f"Average bill per client is: {average:.2f} leva.")
