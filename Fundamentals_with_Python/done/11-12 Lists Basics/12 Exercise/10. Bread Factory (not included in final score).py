current_energy = 100
coins = 100
working_day = input().split("|")
all_events_handled = True

for element in range(len(working_day)):
    current_element = working_day[element].split("-")
    event = current_element[0]
    points = int(current_element[1])

    if event == "rest":
        energy_var = current_energy
        current_energy += points
        if current_energy > 100:
            current_energy = 100
            print(f"You gained {100 - energy_var} energy.")
        else:
            print(f"You gained {points} energy.")
        print(f"Current energy: {current_energy}.")

    elif event == "order":
        if current_energy >= 30:
            print(f"You earned {points} coins.")
            coins += points
            current_energy -= 30
        else:
            current_energy += 50
            print("You had to rest!")
            # all_events_handled = False    #judge wants it commented! It is per the request:
    else:
        ingredient = event
        if coins >= points:
            print(f"You bought {ingredient}.")
            coins -= points
        else:
            all_events_handled = False
            print(f"Closed! Cannot afford {ingredient}.")
            break

if all_events_handled:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")
