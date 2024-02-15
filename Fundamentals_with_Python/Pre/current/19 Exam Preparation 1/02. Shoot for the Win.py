def shooting(targets: list, index_hit: int, successful_hit_count: int):
    # print(f"targets : {targets}")
    print(f"index : {index_hit}")
    print(f"successful_hit_count : {successful_hit_count}")

    if index_hit >= len(targets):
        return [targets, successful_hit_count]
    if index_hit < len(targets):
        print(f"will we hit? {targets[index_hit]} --- {'-1'}")
    if targets[index_hit] != "-1":
        successful_hit_count += 1
        new = int(targets[index_hit])
        for index, element in enumerate(targets):
            if index == index_hit:
                continue
            elif int(element) > new and int(element) != -1:
                targets[index] = str(int(element) - new)
            elif int(element) <= new and int(element) != -1:
                targets[index] = str(int(element) + new)
        targets[index_hit] = "-1"
    # shot_modification = [int(element) for element in targets]
    # print(f"targets after mods: {targets}")
    return [targets,successful_hit_count]

#
# c = 1          # to remove


hit_counter = 0
target_list = list(map(int, input().split()))
# target_list = list(map(int, "24 50 36 70".split()))          # to remove
# target_list = list("24 50 36 70".split())          # to remove

while True:
    # if c == 2:         # to remove
    #     break          # to remove
    # c = 2     # to remove
    command = input()
    # command = "0"       # to remove
    if command == "End":
        target_list = " ".join(target_list)
        print(f"Shot targets: {current_shoot_result[1]} -> {target_list}")
        break
    shooting_index = int(command)
    current_shoot_result = shooting(target_list, shooting_index, hit_counter)
    target_list = current_shoot_result[0]
