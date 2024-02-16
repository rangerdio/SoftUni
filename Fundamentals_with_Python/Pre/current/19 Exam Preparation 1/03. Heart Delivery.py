def cupid_jump(neigh_str_list: list, jump_index: int, hit_count: int, last_pos: int):
    mark = False
    current_position = 0 if jump_index + last_pos >= len(neigh_str_list) else jump_index + last_pos

    if int(neigh_str_list[current_position]) == 0:
        print(f"Place {current_position} already had Valentine's day.")
    else:
        neigh_str_list[current_position] = str(int(neigh_str_list[current_position]) - 2)
        mark = True
    if mark:
        if int(neigh_str_list[current_position]) == 0:
            print(f"Place {current_position} has Valentine's day.")

    return [neigh_str_list, hit_count, current_position]


neighborhood_str_list = input().split("@")
jump_result_list = neighborhood_str_list

hits = 0
last_position = 0
command = input()

while command != "Love!":
    command = command.split()
    command = command[1]
    jump_result_matrix = cupid_jump(neighborhood_str_list, int(command), hits, last_position)
    jump_result_list = jump_result_matrix[0]
    neighborhood_str_list = jump_result_list
    hits = jump_result_matrix[1]
    last_position = jump_result_matrix[2]
    command = input()

val = 0
not_val = 0
for element in jump_result_list:
    if int(element) == 0:
        val += 1
    else:
        not_val += 1

print(f"Cupid's last position was {last_position}.")

if val == len(jump_result_list):
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {not_val} places.")
