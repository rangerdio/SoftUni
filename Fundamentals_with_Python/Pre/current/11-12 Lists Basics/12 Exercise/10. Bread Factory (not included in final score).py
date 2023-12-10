current_energy = 100
coins = 100
working_day = input().split("|")
all_events_handled = True

for element in range(len(working_day)):
    current_element = working_day[element].split("-")
    # current_element[1] = int(current_element[1])

    if current_element[0] == "rest":
        element_energy = int(current_element[1])
        if current_energy == 100:
            print("You gained 0 energy.")
            print(f"Current energy: {current_energy}.")
        elif current_energy + element_energy <= 100:
            current_energy += element_energy
            print(f"You gained {element_energy} energy.")
            print(f"Current energy: {current_energy}.")

        elif (current_energy + element_energy) > 100 > current_energy:
            cur = current_energy
            current_energy = 100
            print(f"You gained {100 - cur} energy.")
            print(f"Current energy: {current_energy}.")

    elif current_element[0] == "order":
        earned = int(current_element[1])
        if current_energy >= 30:
            coins += earned
            current_energy -= 30
            print(f"You earned {earned} coins.")
        else:
            # skipped the order
            earned = 0
            current_energy += 50
            print("You had to rest!")
            all_events_handled = False
    else:
        ingredient = current_element[0]
        if coins >= int(current_element[1]):
            print(f"You bought {ingredient}.")
            coins -= int(current_element[1])
        else:
            all_events_handled = False
            print(f"Closed! Cannot afford {ingredient}.")
            break
if all_events_handled:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")
