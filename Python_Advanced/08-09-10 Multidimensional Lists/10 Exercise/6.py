from collections import deque
field = []
my_initial_position = []
targets = 0
targets_hit = 0
for row in range(5):
    sublist = input().split()
    if 'A' in sublist:
        my_initial_position = [row, sublist.index('A')]
    if 'x' in sublist:
        targets += sublist.count('x')
    field.append(sublist)

hits = []
command_queue = deque([])
n = int(input())
for _ in range(n):
    command_queue.append(input().split())

my_current_position = my_initial_position
while command_queue:
    current_command = command_queue.popleft()
    action = current_command[0]

    if action == "move":
        direction = current_command[1]
        steps = int(current_command[2])
        directions = {
            "up": [-1 * steps, 0],
            "down": [1 * steps, 0],
            "left": [0, -1 * steps],
            "right": [0, 1 * steps]
        }
        my_new_pos_row = my_current_position[0] + directions[direction][0]
        my_new_pos_col = my_current_position[1] + directions[direction][1]
        my_new_pos = [my_new_pos_row, my_new_pos_col]
        if 0 <= my_new_pos[0] < 5 and 0 <= my_new_pos[1] < 5:
            if field[my_new_pos[0]][my_new_pos[1]] == '.':
                field[my_new_pos[0]][my_new_pos[1]] = 'A'
                field[my_current_position[0]][my_current_position[1]] = '.'
            else:
                continue
        else:
            continue

    elif action == "shoot":
        direction = current_command[1]
        directions = {
            "up": [-1, 0],
            "down": [1, 0],
            "left": [0, -1],
            "right": [0, 1]
        }
        current_shoot_pos = my_current_position
        while 0 <= current_shoot_pos[0] < 5 and 0 <= current_shoot_pos[1] < 5:
            new_shoot_pos = [current_shoot_pos[0] + directions[direction][0],
                             current_shoot_pos[1] + directions[direction][1]]
            if 0 <= new_shoot_pos[0] < 5 and 0 <= new_shoot_pos[1] < 5:
                if field[new_shoot_pos[0]][new_shoot_pos[1]] == 'x':
                    hits.append([new_shoot_pos[0], new_shoot_pos[1]])
                    field[new_shoot_pos[0]][new_shoot_pos[1]] = '.'
                    current_shoot_pos = new_shoot_pos
                    targets_hit += 1
                    if targets_hit == targets:
                        print(f'Training completed! All {targets_hit} targets hit.')
                        break
                else:
                    current_shoot_pos = new_shoot_pos
                    continue
            current_shoot_pos = new_shoot_pos

if targets != targets_hit:
    print(f"Training not completed! {targets - targets_hit} targets left.")

print(*hits, sep='\n')
