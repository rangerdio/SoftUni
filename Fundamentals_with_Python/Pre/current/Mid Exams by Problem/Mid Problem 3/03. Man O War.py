def firing(pirate_ship: list, warship: list, index: int, damage: int):
    if len(warship) > index:
        warship[index] -= damage
        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            # ENEMY SHIP IS DOWN AND PROGRAM END
            return
    return [pirate_ship, warship]


def defending(pirate_ship: list, warship: list, start_index: int, end_index: int, damage: int):
    valid_list = []
    for _ in range(len(pirate_ship)):
        valid_list.append(_)
    if start_index in valid_list and end_index in valid_list:
        for index in range(start_index, end_index + 1):
            pirate_ship[index] -= damage
            if pirate_ship[index] <= 0:
                print("You lost! The pirate ship has sunken.")
                # WE LOST. OUR SHIP IS DOWN AND PROGRAM END
                return
    return [pirate_ship, warship]


def repairing(pirate_ship: list, warship: list, index: int, health: int, max_health: int):
    valid_list = []
    for _ in range(len(pirate_ship)):
        valid_list.append(_)
    if index in valid_list:
        pirate_ship[index] += health
        if pirate_ship[index] > max_health:
            pirate_ship[index] = max_health
    return [pirate_ship, warship]


def status(pirate_ship: list, warship: list, max_health: int):
    barer = 20 / 100 * max_health

    unhealthy = [element for element in pirate_ship if element < barer]
    return len(unhealthy)


pirate_ship_status = input().split(">")
warship_status = input().split(">")
max_section_health = int(input())

while True:
    command = input()

    if command == "Retire":
        break

    command_list = command.split()

    if command == "Fire":
        firing(pirate_ship_status, warship_status, int(command_list[1]), int(command_list[2]))
    elif command == "Defend":
        defending(pirate_ship_status, warship_status, int(command_list[1]), int(command_list[2]), int(command_list[3]))
    elif command == "Repair":
        repairing(pirate_ship_status, warship_status, int(command_list[1]), int(command_list[2]), max_section_health)
    elif command == "Status":
        status(pirate_ship_status, warship_status, max_section_health)
