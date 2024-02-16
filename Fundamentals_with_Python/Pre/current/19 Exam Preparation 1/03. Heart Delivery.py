def cupid_jump(neigh_str_list: list, jump_index: int, hit_count: int):
    current_position = 0 if jump_index >= len(neigh_str_list) else jump_index

    return [neigh_str_list, hit_count, current_position]


neighborhood_str_list = "10@10@10@2".split("@")
# neighborhood_str_list = input().split("@")
jump_result_list = neighborhood_str_list

hits = 0
last_position = "no position"

command = input()
while command != "Love":

    jump_result_matrix = cupid_jump(neighborhood_str_list, int(command), hits)
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
if val == len(jump_result_list) - 1:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {not_val} places.")
