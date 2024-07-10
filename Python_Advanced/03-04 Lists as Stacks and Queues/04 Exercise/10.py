from collections import deque

cups_capacity = deque([int(element) for element in input().split()])
bottle_capacity = [int(element) for element in input().split()]

wasted = 0
while bottle_capacity:
    current_cup = cups_capacity.popleft()
    current_bottle = bottle_capacity.pop()

    if current_bottle >= current_cup:  # current_cup <= 0
        # remaining current_bottle value became wasted
        wasted += abs(current_cup - current_bottle)
        if not cups_capacity:
            break
        continue
    else:  # current_bottle < current_cup
        cups_capacity.insert(0, current_cup - current_bottle)
        if not cups_capacity:
            break

if not cups_capacity:
    print("Bottles: ", end="")
    print(*bottle_capacity, sep=" ")

if not bottle_capacity:
    print("Cups:", end="")
    print(*cups_capacity, sep=" ")
print(f"Wasted litters of watter: {wasted}")
