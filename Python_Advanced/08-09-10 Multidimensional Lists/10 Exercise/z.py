from collections import deque

field = []
my_initial_position = []
targets = 0

for row in range(5):
    sublist = input().split()
    if 'A' in sublist:
        my_initial_position = [row, sublist.index('A')]
    targets += sublist.count('x')
    field.append(sublist)

n = int(input())
commands = deque([input().split() for _ in range(n)])

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

hits = []
my_current_position = my_initial_position
targets_hit = 0
training_completed = False

for command in commands:
    action = command[0]

    if action == "move":
        direction = command[1]
        steps = int(command[2])
        next_row, next_col = my_current_position

        for step in range(steps):
            next_row += my_current_position[0] + directions[direction][0]
            next_col += my_current_position[1] + directions[direction][1]

        if 0 <= next_row < 5 and 0 <= next_col < 5 and field[next_row][next_col] == '.':
            my_current_position = [next_row, next_col]
            field[my_current_position[0]][my_current_position[1]] = '.'
            field[my_current_position[0]][my_current_position[1]] = 'A'

    elif action == "shoot":
        direction = command[1]
        shoot_position = my_current_position[:]

        while True:
            shoot_position[0] += directions[direction][0]
            shoot_position[1] += directions[direction][1]

            if 0 <= shoot_position[0] < 5 and 0 <= shoot_position[1] < 5:
                if field[shoot_position[0]][shoot_position[1]] == '.':
                    continue
                elif field[shoot_position[0]][shoot_position[1]] == 'x':
                    hits.append([shoot_position[0], shoot_position[1]])
                    field[shoot_position[0]][shoot_position[1]] = '.'
                    targets_hit += 1
                    if targets_hit == targets:
                        training_completed = True
                    break
            else:
                break
    if training_completed:
        break

if training_completed:
    print(f"Training completed! All {targets_hit} targets hit.")
else:
    print(f"Training not completed! {targets - targets_hit} targets left.")

for hit in hits:
    print(hit)
