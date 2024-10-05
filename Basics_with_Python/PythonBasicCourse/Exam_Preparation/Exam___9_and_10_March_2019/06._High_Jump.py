target = int(input())
start = target - 30
middle_target = start
fail = False
success = False
win = False
jump_counter = 0
jump_high = 0
while True:
    result = 0
    for _ in range(1, 4):
        result = int(input())
        jump_counter += 1
        if result > target and middle_target >= target:
            win = True
            jump_high = result
            break
        elif result > middle_target:
            break
    if win:
        break
    if result <= middle_target:
        fail = True
        jump_high = result
        break
    middle_target += 5
if fail:
    print(f"Tihomir failed at { middle_target}cm after {jump_counter} jumps.")
elif success or win:
    print(f"Tihomir succeeded, he jumped over {middle_target}cm after {jump_counter} jumps.")
