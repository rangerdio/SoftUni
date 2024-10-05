from collections import deque
moneys = [int(x) for x in input().split()]
prices = deque([int(x) for x in input().split()])
food_eaten = 0

while moneys and prices:
    money = moneys.pop()
    price = prices.popleft()

    if money == price:
        food_eaten += 1

    elif money > price:
        food_eaten += 1
        if len(moneys) > 1:
            moneys[-1] += (money - price)

if food_eaten > 3:  # any bigger than 3
    print(f'Gluttony of the day! Henry ate {food_eaten} foods.')
elif food_eaten == 1:
    print(f'Henry ate: {food_eaten} food.')
elif food_eaten:    # 2 or 3, because if >3 or 1 we will not come here
    print(f'Henry ate: {food_eaten} foods.')
else:
    print('Henry remained hungry. He will try next weekend again.')

# from collections import deque
# moneys = [int(x) for x in input().split()]
# prices = deque([int(x) for x in input().split()])
# food_eaten = 0
#
# while moneys and prices:
#     # money = moneys.pop()
#     # price = prices.popleft()
#
#     if moneys[-1] == prices[0]:
#         food_eaten += 1
#         moneys.pop()
#
#     elif moneys[-1] > prices[0]:
#         food_eaten += 1
#         if len(moneys) > 1:
#             change = moneys[-1] - prices[0]
#             moneys.pop()
#             moneys[-1] += change
#         else:
#             change = 0
#             moneys.pop()
#             moneys.append(change)
#
#     else:
#         moneys.pop()
#     prices.popleft()
#
# if food_eaten > 3:  # any bigger than 3
#     print(f'Gluttony of the day! Henry ate {food_eaten} foods.')
# elif food_eaten == 1:
#     print(f'Henry ate: {food_eaten} food.')
# elif food_eaten:    # 2 or 3, because if >3 or 1 we will not come here
#     print(f'Henry ate: {food_eaten} foods.')
# else:
#     print('Henry remained hungry. He will try next weekend again.')
