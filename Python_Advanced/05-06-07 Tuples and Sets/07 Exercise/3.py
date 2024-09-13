from collections import deque
chocolate = deque([int(x) for x in input().split(', ')])
cups_milk = deque([int(x) for x in input().split(', ')])
milkshakes = 0

while chocolate and cups_milk and milkshakes < 5:
    if chocolate[-1] <= 0 and cups_milk[0] <= 0:
        chocolate.pop()
        cups_milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if cups_milk[0] <= 0:
        cups_milk.popleft()
        continue

    if chocolate[-1] == cups_milk[0]:
        chocolate.pop()
        cups_milk.popleft()
        milkshakes += 1
    else:
        cups_milk.rotate(-1)
        chocolate[-1] -= 5

print('Great! You made all the chocolate milkshakes needed!') if milkshakes == 5 else print('Not enough milkshakes.')

if not chocolate:
    print('Chocolate: empty')
else:
    print(f'Chocolate: {", ".join(map(str, chocolate))}')

if not cups_milk:
    print('Milk: empty')
else:
    print(f'Milk: {", ".join(map(str, cups_milk))}')

