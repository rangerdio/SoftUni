def idx_validation(data_list: list, index: int):
    valid_list = []
    for _ in range(len(data_list)):
        valid_list.append(_)
    if index in valid_list:
        return True
    else:
        return False


def shoot_manipulation(targets: list, index: int, value: int):
    targets[index] -= value
    if targets[index] <= 0:
        element_to_remove = targets[index]
        targets.remove(element_to_remove)
    return targets


def add_manipulation(targets: list, index: int, value: int):
    new_element = targets[index]
    targets.insert(index, new_element)
    return targets


def strike_manipulation(targets: list, index: int, value: int):
    targets = targets[:index - 1:] + targets[index + value + 1:]
    return targets


target_list = list(map(int, input().split()))
result_list = []
while True:
    command = input()
    if command == "End":
        result = [str(element) for element in target_list]
        print(f'{"|".join(result)}')
        break
    command_list = command.split()
    if command_list[0] == "Shoot":
        if idx_validation(target_list, int(command_list[1])):
            result_list = shoot_manipulation(target_list, int(command_list[1]), int(command_list[2]))
        else:
            result_list = target_list

    elif command_list[0] == "Add":
        if idx_validation(target_list, int(command_list[1])):
            result_list = add_manipulation(target_list, int(command_list[1]), int(command_list[2]))
        else:
            print("Invalid placement!")
            result_list = target_list

    elif command_list[0] == "Strike":
        if idx_validation(target_list, int(command_list[1])) and idx_validation(target_list, int(command_list[1]) - 1)\
                and idx_validation(target_list, int(command_list[1]) + 1):
            result_list = strike_manipulation(target_list, int(command_list[1]), int(command_list[2]))
        else:
            print("Strike missed!")
            result_list = target_list

    target_list = result_list
