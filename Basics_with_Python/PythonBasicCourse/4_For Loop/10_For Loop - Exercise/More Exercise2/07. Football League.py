stadium_capacity = int(input())
total_fans = int(input())
a = 0
b = 0
v = 0
g = 0
for _num in range(1, total_fans + 1):
    fan_sector = input()
    if fan_sector == "A":
        a += 1
    elif fan_sector == "B":
        b += 1
    if fan_sector == "V":
        v += 1
    elif fan_sector == "G":
        g += 1
fans_sector_a = a * 100 / total_fans
fans_sector_b = b * 100 / total_fans
fans_sector_v = v * 100 / total_fans
fans_sector_g = g * 100 / total_fans
total_fans = 100 * (a + b + v + g) / stadium_capacity
print(f"{fans_sector_a:.2f}%")
print(f"{fans_sector_b:.2f}%")
print(f"{fans_sector_v:.2f}%")
print(f"{fans_sector_g:.2f}%")
print(f"{total_fans:.2f}%")
