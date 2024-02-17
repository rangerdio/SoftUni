def loot():
    return "asd"


def drop():
    return "123"


def steal():
    return "123"


treasure_chest = input().split("|")
while True:
    command = input()

    if command == "Yohoho!":
        break
    command_list = command.split()

    if command_list[0] == "Loot":
        pass
    elif command_list[0] == "Drop":
        pass
    elif command_list[0] == "steal":
        pass
