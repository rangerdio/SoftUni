budged = float(input())
num_vid = int(input())
num_cpu = int(input())
num_ram = int(input())
tot_vid = 250 * num_vid
price_cpu = tot_vid * 0.35
price_ram = tot_vid * 0.1
tot_cpu = price_cpu * num_cpu
tot_ram = price_ram * num_ram
total = tot_ram + tot_cpu + tot_vid
if num_vid > num_cpu:
    total = 0.85 * total
if total <= budged:
    print(f"You have {budged - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budged:.2f} leva more!")
