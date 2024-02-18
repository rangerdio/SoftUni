def manipulation(targets):
    return "123"


target_list = input().split()
while True:
    command = input()
    if command == "End":
        print(f'{" ".join(target_list)}')
        break
    command_list = command.split()
    result_list = manipulation(target_list)
    target_list = result_list


