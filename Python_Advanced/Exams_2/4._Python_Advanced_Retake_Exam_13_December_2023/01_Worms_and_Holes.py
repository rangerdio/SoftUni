from collections import deque
worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])
matches = 0

while worms and holes:
    if worms[-1] <= 0:
        worms.pop()
        continue

    if worms[-1] == holes[0]:
        matches += 1
        worms.pop()
        holes.popleft()

    else:
        holes.popleft()
        worms[-1] -= 3

print(f'Matches: {matches}') if matches else print('There are no matches.')

if worms and not holes:
    print(f'Worms left: {", ".join(str(x) for x in worms)}')
elif not worms and not holes:
    print(f'Every worm found a suitable hole!')
elif not worms and matches:
    print('Worms left: none')

print(f'Holes left: {", ".join(str(x) for x in holes)}') if holes else print('Holes left: none')
