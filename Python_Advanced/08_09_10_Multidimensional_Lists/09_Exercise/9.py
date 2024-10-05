from collections import deque
n = int(input())
movement = deque(input().split())
start_coordinates = []
field = []
coal = 0

for row in range(n):
    current_row = input().split()
    if "s" in current_row:
        start_coordinates = [row, current_row.index('s')]
    if "c" in current_row:
        coal += current_row.count('c')
    field.append(current_row)

coal_counter = 0
current_coordinate = start_coordinates
new_coordinate = start_coordinates
ended = False

while movement:
    current_command = movement.popleft()
    move = {
        'up': [current_coordinate[0] - 1, current_coordinate[1]],
        'down': [current_coordinate[0] + 1, current_coordinate[1]],
        'left': [current_coordinate[0], current_coordinate[1] - 1],
        'right': [current_coordinate[0], current_coordinate[1] + 1]
    }

    if (move[current_command][0] < 0 or move[current_command][0] >= n) or (
            move[current_command][1] < 0 or move[current_command][1] >= n):
        continue
    else:
        new_coordinate = move[current_command]
        field[current_coordinate[0]][current_coordinate[1]] = '*'

        destination = field[new_coordinate[0]][new_coordinate[1]]

        if destination == 'e':
            field[new_coordinate[0]][new_coordinate[1]] = 's'
            print(f'Game over! ({new_coordinate[0]}, {new_coordinate[1]})')
            ended = True
            break
        elif destination == 'c':
            field[new_coordinate[0]][new_coordinate[1]] = 's'
            coal_counter += 1
            if coal_counter == coal:
                print(f'You collected all coal! ({new_coordinate[0]}, {new_coordinate[1]})')
                ended = True
                break
        elif destination == '*':
            field[new_coordinate[0]][new_coordinate[1]] = 's'
    current_coordinate = new_coordinate

if not ended:
    print(f'{coal - coal_counter} pieces of coal left. ({new_coordinate[0]}, {new_coordinate[1]})')
