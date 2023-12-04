funds_required = int(input())
funds_collected = 0
counter = 1
cash_sum = 0
card_sum = 0
cash_counter = 0
card_counter = 0
bill = 0
while funds_collected < funds_required:
    bill = input()
    if bill == "End":
        break
    bill = int(bill)
    if counter % 2 != 0:  # cash only
        if bill <= 100:
            print("Product sold!")
            funds_collected += bill
            cash_sum += bill
            counter += 1
            cash_counter += 1
        else:
            print("Error in transaction!")
            counter += 1
    else:  # card only
        if bill >= 10:
            print("Product sold!")
            funds_collected += bill
            card_sum += bill
            counter += 1
            card_counter += 1
        else:
            print("Error in transaction!")
            counter += 1
if bill == "End":
    # print("Error tests:  funds collected = ",funds_collected)
    print("Failed to collect required money for charity.")
else:
    average_cash = cash_sum / cash_counter
    average_card = card_sum / card_counter
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")
