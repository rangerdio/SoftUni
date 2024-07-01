from collections import deque
food_amount = int(input())

orders = deque(map(int, input().split()))
print(max(orders))

while orders:
    current_order = orders.popleft()
    if food_amount - current_order >= 0:
        food_amount -= current_order
    else:
        print("Orders left:", current_order, end=" ")
        print(*orders, sep=" ")
        break
else:
    print("Orders complete")
