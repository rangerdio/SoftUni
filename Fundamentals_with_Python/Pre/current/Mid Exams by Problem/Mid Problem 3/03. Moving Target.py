def index_validation(data_list: list, index: int):
    valid_list = []
    for _ in range(len(data_list)):
        valid_list.append(_)
    if index in valid_list:
        return True
    else:
        return False


def manipulation(targets: list, index: int, value: int):

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
        result_list = manipulation(target_list, int(command_list[1]), int(command_list[2]))
    elif command_list[0] == "Add":
        result_list = manipulation(target_list, int(command_list[1]), int(command_list[2]))
    elif command_list[0] == "Add":
        result_list = manipulation(target_list, int(command_list[1]), int(command_list[2]))
    target_list = result_list
