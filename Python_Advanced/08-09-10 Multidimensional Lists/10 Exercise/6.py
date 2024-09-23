from collections import deque

field = []
my_current_position = []
targets = 0

for row in range(5):
    sublist = input().split()
    if 'A' in sublist:
        my_current_position = [row, sublist.index('A')]
    targets += sublist.count('x')
    field.append(sublist)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

hits = []
targets_hit = 0

for _ in range(int(input())):
    command = input().split()

    if command[0] == "shoot":
        next_row = my_current_position[0] + directions[command[1]][0]
        next_col = my_current_position[1] + directions[command[1]][1]

        while 0 <= next_row < 5 and 0 <= next_col < 5:
            if field[next_row][next_col] == 'x':
                hits.append([next_row, next_col])
                field[next_row][next_col] = '.'
                targets_hit += 1
                break   # target is git, moving to next command
            next_row += directions[command[1]][0]  # no target here, so we continue the bullet direction
            next_col += directions[command[1]][1]

        if targets_hit == targets:
            print(f"Training completed! All {targets_hit} targets hit.")
            break

    elif command[0] == "move":
        direction = command[1]
        steps = int(command[2])
        next_row = my_current_position[0] + directions[direction][0] * steps
        next_col = my_current_position[1] + directions[direction][1] * steps

        if 0 <= next_row < 5 and 0 <= next_col < 5 and field[next_row][next_col] == '.':
            field[next_row][next_col] = 'A'
            field[my_current_position[0]][my_current_position[1]] = '.'
            my_current_position = [next_row, next_col]

if targets_hit != targets:
    print(f"Training not completed! {targets - targets_hit} targets left.")

for hit in hits:
    print(hit)
