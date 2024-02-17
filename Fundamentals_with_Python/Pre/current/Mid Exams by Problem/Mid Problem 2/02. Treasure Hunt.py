def loot(treasure: list, cmd: list):
    for item in cmd:
        if item not in treasure:
            treasure.insert(0, item)
    return treasure


def drop(treasure: list, cmd: list):
    cmd = int(cmd[0])
    treasure.append(treasure.pop(cmd))
    return treasure


def steal(treasure: list, cmd: list):
    cmd = int(cmd[0])
    if cmd >= len(treasure):
        treasure = []
    else:
        stolen_items = []
        for _ in range(cmd):
            stolen_items.append(treasure.pop(-1))
        print(stolen_items[::-1])
    return treasure



treasure_chest = input().split("|")
while True:
    command = input()

    if command == "Yohoho!":
        break
    command_list = command.split()

    if command_list[0] == "Loot":
        command_list.remove("Loot")
        resulted_treasure = loot(treasure_chest, command_list)
        treasure_chest = resulted_treasure

    elif command_list[0] == "Drop":
        command_list.remove("Drop")
        resulted_treasure = drop(treasure_chest, command_list)
        treasure_chest = resulted_treasure

    elif command_list[0] == "Steal":
        command_list.remove("Steal")
        resulted_treasure = steal(treasure_chest, command_list)
        treasure_chest = resulted_treasure

print(treasure_chest)
