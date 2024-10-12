from collections import deque
worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])
matches = 0
worms_total= len(worms)

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1
    else:
        worm -= 3
        if worm > 0:
            worms.append(worm)

if matches > 0:
    print(f'Matches: {matches}')
else:
    print('There are no matches.')

if matches != worms_total:
    # If not all worms found a suitable hole, print the remaining worms.
    print(f"Worms left: {', '.join(map(str, worms))}" if worms else "Worms left: none")
else:
    # If all worms found suitable holes, print a message.
    print("Every worm found a suitable hole!")

if holes:
    print(f'Holes left: {", ".join(str(x) for x in holes)}')
else:
    print('Holes left: none')


# from collections import deque
# worms = [int(x) for x in input().split()]
# holes = deque([int(x) for x in input().split()])
# matches = 0
#
# while worms and holes:
#     if worms[-1] != holes[0]:
#         if worms[-1] <= 0:
#             worms.pop()
#         else:
#             holes.popleft()
#             worms[-1] -= 3
#     elif worms[-1] == holes[0]:
#         matches += 1
#         worms.pop()
#         holes.popleft()
#
# print(f'Matches: {matches}') if matches else print('There are no matches.')
#
# if not worms and not holes:
#     print(f'Every worm found a suitable hole!')
# elif not worms and holes:
#     print('Worms left: none')
# elif worms:
#     print(f'Worms left: {", ".join(str(x) for x in worms)}')
#
# print(f'Holes left: {", ".join(str(x) for x in holes)}') if holes else print('Holes left: none')
