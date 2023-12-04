import math
people = int(input())
pool_tax = float(input())
bed_price = float(input())
umbrella_price = float(input())

tax_entrance_total = people * pool_tax
umbrellas_used = math.ceil(people / 2)
tax_umbrella = umbrellas_used * umbrella_price
beds_used = math.ceil(((people * 75) / 100))
tax_bed = bed_price * beds_used

total = tax_entrance_total + tax_bed + tax_umbrella
print(f"{total:.2f} lv.")