energy = int(input())
target_energy_distance = 0
win_counter = 0
lost = False
while True:
    command = input()
    if command == "End of battle":
        break
    else:
        target_energy_distance = int(command)

    if energy < target_energy_distance:
        lost = True
        break
    if energy == target_energy_distance:
        win_counter += 1
        energy -= target_energy_distance
        if win_counter % 3 == 0:
            energy += win_counter

    elif energy > target_energy_distance:
        win_counter += 1
        energy -= target_energy_distance
        if win_counter % 3 == 0:
            energy += win_counter

if lost:
    print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
else:
    print(f"Won battles: {win_counter}. Energy left: {energy}")