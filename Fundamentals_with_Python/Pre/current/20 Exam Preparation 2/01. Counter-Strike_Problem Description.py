def counter_strike(energy: int):
    target_energy_distance = 0
    win_counter = 0

    while True:
        command = input()
        if command == "End of battle":
            print(f"Won battles: {win_counter}. Energy left: {energy}")
            break
        else:
            target_energy_distance = int(command)

        if energy >= target_energy_distance:
            win_counter += 1
            energy -= target_energy_distance
            energy += win_counter if win_counter % 3 == 0 else 0
        else:
            print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
            break
    return


counter_strike(int(input()))
