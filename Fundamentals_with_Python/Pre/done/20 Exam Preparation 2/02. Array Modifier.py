def array_modifier(start_list: list, command_list: list):
    if command_list[0] == "decrease":
        start_list = [element - 1 for element in start_list]
    elif command_list[0] == "swap":
        index1, index2 = int(command_list[1]), int(command_list[2])
        start_list[index1], start_list[index2] = start_list[index2], start_list[index1]
    elif command_list[0] == "multiply":
        index1, index2 = int(command_list[1]), int(command_list[2])
        start_list[index1] *= start_list[index2]
    return start_list


st_list = list(map(int, input().split()))
modified_list = []

while True:
    command = input()
    if command == "end":
        break
    cmd_list = command.split()
    modified_list = array_modifier(st_list, cmd_list)
    st_list = modified_list

print(", ".join(str(element) for element in modified_list))
