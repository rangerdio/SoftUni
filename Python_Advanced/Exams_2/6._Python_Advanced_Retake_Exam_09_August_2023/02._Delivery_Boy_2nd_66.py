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
collected = False
delivered = False
cancelled = False

while True:
    command = input()
    row, col = player_position
    new_row = row + directions[command][0]
    new_col = col + directions[command][1]

    if 0 <= new_row < field_rows and 0 <= new_col < field_cols:
        if field[new_row][new_col] == '*':
            continue
        elif field[new_row][new_col] == "A":
            if collected:
                field[new_row][new_col] = "P"
                field[init_player_position[0]][init_player_position[1]] = 'B'
                player_position = [row, col]
                if field[row][col] != "R":
                    field[row][col] = '.'

        elif field[new_row][new_col] == 'P':
            field[new_row][new_col] = 'R'
            player_position = [new_row, new_col]
            if field[row][col] != "R":
                field[row][col] = '.'
    else:
        cancelled = True
        break

if cancelled:
    field[init_player_position[0]][init_player_position[1]] = ' '

if collected:
    print('Pizza is collected. 10 minutes for delivery.')
    if delivered:
        print('Pizza is delivered on time! Next order...')
    elif cancelled:
        print('The delivery is late. Order is canceled.')
elif cancelled:
    print('The delivery is late. Order is canceled.')

for row in field:
    print(f'{"".join(row)}')
