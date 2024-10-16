from collections import deque

caffeines = [int(x) for x in input().split(', ')]
drinks = deque([int(x) for x in input().split(', ')])

maximum_allowed, total_drank = 300, 0
while caffeines and drinks:

    caffeine = caffeines.pop()
    current_drink = drinks.popleft()
    cafeine_in_current_drink = caffeine * current_drink
    if cafeine_in_current_drink + total_drank <= maximum_allowed:
        total_drank += cafeine_in_current_drink
    else:
        drinks.append(current_drink)
        total_drank -= 30
        if total_drank < 0:
            total_drank = 0

print(f'Drinks left: {", ".join(str(x) for x in drinks)}') if drinks else \
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_drank} mg caffeine.")
