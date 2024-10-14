from collections import deque
effects = deque([int(x) for x in input().split(',')])
casings = [int(x) for x in input().split(',')]
bombs_data = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120
}
bombs_created = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}
pouch_is_full = None
while effects and casings:
    current_effect = effects.popleft()
    current_casing = casings.pop()
    action = current_effect + current_casing

    if action in bombs_data.values():
        for bomb_name, bomb_value in bombs_data.items():
            if action == bomb_value:
                bombs_created[bomb_name] += 1
                break
        pouch_is_full = True
        for bomb_name, bomb_value in bombs_created.items():
            if bomb_value < 3:
                pouch_is_full = False
                break
        if pouch_is_full:
            break
    else:
        current_casing -= 5
        effects.appendleft(current_effect)
        casings.append(current_casing)


if pouch_is_full:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join(str(effect) for effect in effects)}") if effects else print("Bomb Effects: empty")
print(f"Bomb Casings: {', '.join(str(casing) for casing in casings)}") if casings else print("Bomb Casings: empty")
bombs_created_sorted = sorted(bombs_created.items(), key=lambda x: x[0])
for bomb_name, count in bombs_created_sorted:
    print(f"{bomb_name}: {count}")
