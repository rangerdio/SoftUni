deposit_amount = float(input())
months = int(input())
yearly_interest = float(input())

total_interest = deposit_amount + months * ((deposit_amount * yearly_interest / 100) / 12)
print(total_interest)
