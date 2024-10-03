from collections import deque
bees = deque([int(x) for x in input().split(' ')])
eaters = [int(x) for x in input().split(' ')]

while bees and eaters:
    current_bee_group = bees.popleft()
    current_eater_group = eaters.pop()

    if current_bee_group < 7 * current_eater_group:
        eaters.append(current_eater_group - current_bee_group // 7)

    elif current_bee_group == 7 * current_eater_group:
        continue
    else:
        bees.append(current_bee_group - 7 * current_eater_group)

print("The final battle is over!")
if not bees and not eaters:
    print("But no one made it out alive!")
elif bees:
    print(f'Bee groups left: {", ".join(str(x) for x in bees)}')
else:
    print(f'Bee-eater groups left: {", ".join(str(x) for x in eaters)}')
