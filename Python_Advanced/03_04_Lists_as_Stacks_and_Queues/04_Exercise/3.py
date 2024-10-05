# from collections import deque
# food_amount = int(input())
#
# orders = deque(map(int, input().split()))
# print(max(orders))
#
# while orders:
#     current_order = orders.popleft()
#     if food_amount - current_order >= 0:
#         food_amount -= current_order
#     else:
#         print("Orders left:", current_order, *orders)
#         break
# else:
#     print("Orders complete")


from collections import deque
food_amount = int(input())

orders = deque(map(int, input().split()))
print(max(orders))

for order in orders.copy():
    if food_amount < order:
        print(f"Orders left:", *orders)
        break
    else:
        food_amount -= order
        orders.popleft()
else:
    print("Orders complete")
