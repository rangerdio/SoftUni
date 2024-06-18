def firing(pirate_ship: list, warship: list, index: int, damage: int, kk: str):
    if len(warship) > index:
        warship[index] -= damage
        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            # ENEMY SHIP IS DOWN AND PROGRAM END
            kk = "bbb"
            return [kk, pirate_ship, warship]
    return [kk, pirate_ship, warship]


def defending(pirate_ship: list, warship: list, start_index: int, end_index: int, damage: int, kk: str):
    valid_list = []
    for _ in range(len(pirate_ship)):
        valid_list.append(_)
    if start_index in valid_list and end_index in valid_list:
        for index in range(start_index, end_index + 1):
            pirate_ship[index] -= damage
            if pirate_ship[index] <= 0:
                print("You lost! The pirate ship has sunken.")
                # WE LOST. OUR SHIP IS DOWN AND PROGRAM END
                kk = "bbb"
                return [kk, pirate_ship, warship]
    return [kk, pirate_ship, warship]


def repairing(pirate_ship: list, warship: list, index: int, health: int, max_health: int, kk: str):
    valid_list = []
    for _ in range(len(pirate_ship)):
        valid_list.append(_)
    if index in valid_list:
        pirate_ship[index] += health
        if pirate_ship[index] > max_health:
            pirate_ship[index] = max_health
    return [kk, pirate_ship, warship]


def status(pirate_ship: list, max_health: int):
    barer = 20 / 100 * max_health

    unhealthy = [element for element in pirate_ship if element < barer]
    return f"{len(unhealthy)} sections need repair."


pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
max_section_health = int(input())

while True:
    command = input()
    kkk = "aaa"
    if command == "Retire":
        print(f"Pirate ship status: {sum(pirate_ship_status)}")
        print(f"Warship status: {sum(warship_status)}")
        break

    command_list = command.split()
    if command_list[0] == "Fire":
        result = firing(pirate_ship_status, warship_status, int(command_list[1]), int(command_list[2]), kkk)
        if result[0] == "bbb":
            break
        else:
            pirate_ship_status = result[1]
            warship_status = result[2]

    elif command_list[0] == "Defend":
        result = defending(pirate_ship_status, warship_status, int(command_list[1]), int(command_list[2]), int(command_list[3]), kkk)
        if result[0] == "bbb":
            break
        else:
            pirate_ship_status = result[1]
            warship_status = result[2]

    elif command_list[0] == "Repair":
        result = repairing(pirate_ship_status, warship_status, int(command_list[1]), int(command_list[2]), max_section_health, kkk)
        pirate_ship_status = result[1]
        warship_status = result[2]

    elif command_list[0] == "Status":
        print(status(pirate_ship_status, max_section_health))
