months = int(input())
water = 20
internet = 15
others_total = 0
electricity_total = 0
for _num in range(1, months + 1):
    electricity = float(input())
    electricity_total += electricity
    others_total += (water + electricity + internet) * 1.2

print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {(water * months):.2f} lv")
print(f"Internet: {(internet * months):.2f} lv")
print(f"Other: {others_total:.2f} lv")
print(f"Average: {((water * months + internet * months + others_total + electricity_total) / months):.2f} lv")
