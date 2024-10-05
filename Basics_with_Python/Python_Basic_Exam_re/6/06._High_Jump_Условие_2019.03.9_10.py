target_height = int(input())
jump_counter = 0
is_fail = False
h = 0
is_prepared = False

start_height = target_height - 30

for height in range(start_height, target_height + 1, 5):
    is_success = False
    for jump in range(1, 4):
        jump_height = int(input())
        jump_counter += 1
        if jump_height > height:
            is_success = True
            break
    if not is_success:
        is_fail = True
        h = height
        break
    if height == target_height and is_success:
        h = height
        is_prepared = True
        break

if is_fail:
    print(f"Tihomir failed at {h}cm after {jump_counter} jumps.")
if is_prepared:
    print(f"Tihomir succeeded, he jumped over {h}cm after {jump_counter} jumps.")
