def shooting(targets: list, index_hit: int, successful_hit_count: int):

    if index_hit >= len(targets):
        return [targets, successful_hit_count]

    if targets[index_hit] != -1:
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
    return [targets, successful_hit_count]


hit_counter = 0
target_list = list(map(int, input().split()))


while True:
    command = input()
    if command == "End":
        target_list = " ".join(target_list)
        print(f"Shot targets: {current_shoot_result[1]} -> {target_list}")
        break
    shooting_index = int(command)
    current_shoot_result = shooting(target_list, shooting_index, hit_counter)
    target_list = current_shoot_result[0]
    hit_counter = current_shoot_result[1]
