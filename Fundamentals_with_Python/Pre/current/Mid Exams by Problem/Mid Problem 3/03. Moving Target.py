def index_validation(data_list: list, index: int):
    valid_list = []
    for _ in range(len(data_list)):
        valid_list.append(_)
    if index in valid_list:
        return True
    else:
        return False


def shoot_manipulation(targets: list, index: int, value: int):
    if index_validation(targets, index):
        pass

    return "123"


def add_manipulation(targets: list, index: int, value: int):
    if index_validation(targets, index):
        pass

    return "123"


def strike_manipulation(targets: list, index: int, value: int):
    if index_validation(targets, index):
        pass

    return "123"


target_list = input().split()
result_list = []
while True:
    command = input()
    if command == "End":
        print(f'{" ".join(target_list)}')
        break
    command_list = command.split()
    if command_list[0] == "Shoot":
        if index_validation(target_list, int(command_list[1])):
            result_list = shoot_manipulation(target_list, int(command_list[1]), int(command_list[2]))
        else:
            result_list = target_list

    elif command_list[0] == "Add":
        if index_validation(target_list, int(command_list[1])):
            result_list = shoot_manipulation(target_list, int(command_list[1]), int(command_list[2]))
        else:
            print("Invalid placement!")
            result_list = target_list

    elif command_list[0] == "Strike":
        if index_validation(target_list, int(command_list[1])):
            result_list = shoot_manipulation(target_list, int(command_list[1]), int(command_list[2]))
        else:
            print("Strike missed!")
            result_list = target_list

    target_list = result_list
