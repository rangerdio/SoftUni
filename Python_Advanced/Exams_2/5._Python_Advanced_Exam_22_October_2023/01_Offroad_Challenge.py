from collections import deque
fuels = [int(x) for x in input().split()]
indexes = deque([int(x) for x in input().split()])
altitudes = deque([int(x) for x in input().split()])
TOP = len(altitudes)
reached = 0
reached_alt = ''

while fuels and indexes:
    fuel = fuels.pop()
    index = indexes.popleft()
    altitude = altitudes.popleft()

    result = fuel - index
    if result >= altitude:
        reached += 1
        reached_alt += f' Altitude {reached},'
        print(f'John has reached: Altitude {reached}')
    else:
        print(f'John did not reach: Altitude {reached + 1}')
        break

if reached == TOP:
    print('John has reached all the altitudes and managed to reach the top!')
elif reached > 0:
    print(f'John failed to reach the top.\nReached altitudes:{reached_alt[:-1]}')
elif not reached:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
