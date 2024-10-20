import math
group_size = int(input())
days = int(input())
coins = 0
for day in range(1, days + 1):
    if day % 15 == 0:
        group_size += 5
    if day % 10 == 0:
        group_size -= 2
    coins = coins + 50 - 2 * group_size
    if day % 3 == 0:
        coins = coins - 3 * group_size
    if day % 5 == 0:
        coins = coins + 20 * group_size
        if day % 3 == 0:
            coins = coins - 2 * group_size
coins_per_companion = math.floor(coins / group_size)
print(coins)
print(f"{group_size} companions received {coins_per_companion} coins each.")
