energy = int(input())
target_energy_distance = 0
win_counter = 0
lost = False
while energy > 0:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {win_counter}. Energy left: {energy}")
        break
    else:
        target_energy_distance = int(command)

    if energy > target_energy_distance:
        win_counter += 1
        energy -= target_energy_distance
        if 0 != win_counter % 3 == 0:
            energy += win_counter
        # print(f"--- Target distance {target_energy_distance} ; counter: {win_counter};  Current Energy: {energy}")
    elif energy == target_energy_distance:
        energy -= target_energy_distance
        win_counter += 1
        if 0 != win_counter % 3 == 0:
            energy += win_counter
        # print(f"--- Target distance {target_energy_distance} ; counter: {win_counter};  Current Energy: {energy}")
        lost = True
        break
    elif energy < target_energy_distance:
        lost = True
        # print(f"--- LOST  Target distance {target_energy_distance} ; counter: {win_counter};  Current Energy: {energy}")
        break
if lost:
    print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
