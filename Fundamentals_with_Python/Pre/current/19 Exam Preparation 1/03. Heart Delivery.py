def shooting(targets: list, index: int, current_hits: int, special: list):
    print(f"targets : {targets}")
    print(f"index : {index}")
    print(f"current_hits : {current_hits}")
    print(f"special indexes {special}")
    if index not in special:
        if index != -1:
            index = -1
            current_hits += 1

    return "!23"


def mark_special_indexes(asd: list):
    special_list = [index for index, element in enumerate(asd) if element == -1]
    return special_list


c = 1  # to remove

hit_counter = 0
# target_and_value_list = list(map(int, input().split()))
target_list = list(map(int, "24 50 36 70".split()))  # to remove
special_indexes = mark_special_indexes(target_list)

while True:
    if c == 2:  # to remove
        break  # to remove
    c = 2
    # command = input()
    command = "0"  # to remove
    if command == "End":
        break
    shooting_index = int(command)
    current_shoot_result = shooting(target_list, shooting_index, hit_counter, special_indexes)
    target_list = current_shoot_result
