def shooting(targets: list, index: int):
    return "!23"


target_and_value_list = list(map(int, input().split()))
while True:
    command = input()
    if command == "End":
        break
    shooting_index = int(command)
    current_shoot_result = shooting(target_and_value_list, shooting_index)
    target_and_value_list = current_shoot_result
