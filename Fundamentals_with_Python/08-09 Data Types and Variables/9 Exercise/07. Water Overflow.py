n = int(input())
capacity = 255
total = 0
for _ in range(n):
    liters = int(input())
    total += liters
    if capacity < total:
        print("Insufficient capacity!")
        total -= liters
print(total)
