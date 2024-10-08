field_rows, field_cols = [int(x) for x in input().split()]
field = []
player_position = []
init_player_position = []
pizza_position = []

for row in range(field_rows):
    line = list(input())
    if 'B' in line:
        player_position = [row, line.index('B')]
        init_player_position = [row, line.index('B')]
    elif 'P' in line:
        pizza_position = [row, line.index('P')]
    field.append(line)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    command = input()
    row, col = player_position
    new_row = row + directions[command][0]
    new_col = col + directions[command][1]

    if not 0 <= new_row < field_rows or not 0 <= new_col < field_cols:
        print('The delivery is late. Order is canceled.')
        field[init_player_position[0]][init_player_position[1]] = ' '
        break

    if field[new_row][new_col] == '*':
        continue
    elif field[new_row][new_col] == '-' or field[new_row][new_col] == '.':
        player_position = [new_row, new_col]
        field[new_row][new_col] = 'B'
        if field[row][col] != 'R':
            field[row][col] = '.'
        continue
    elif field[new_row][new_col] == 'P':
        print('Pizza is collected. 10 minutes for delivery.')
        player_position = [new_row, new_col]
        field[new_row][new_col] = 'R'
        field[row][col] = '.'
        continue
    elif field[new_row][new_col] == 'A':
        print('Pizza is delivered on time! Next order...')
        field[new_row][new_col] = 'P'
        if field[row][col] != 'R':
            field[row][col] = '.'
        field[init_player_position[0]][init_player_position[1]] = 'B'
        break

for row in field:
    print(f'{"".join(row)}')
