field_rows, field_cols = [int(x) for x in input().split()]
field = []
row, col, init_row, init_col = 0, 0, 0, 0
command = "r"

for r in range(field_rows):
    line = list(input())
    if 'B' in line:
        row, col = [r, line.index('B')]
        init_row, init_col = [r, line.index('B')]
    field.append(line)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while command:
    command = input()
    new_row = row + directions[command][0]
    new_col = col + directions[command][1]

    if not (0 <= new_row < field_rows and 0 <= new_col < field_cols):
        print('The delivery is late. Order is canceled.')
        field[init_row][init_col] = ' '
        break

    if field[new_row][new_col] == '*':
        continue
    elif field[new_row][new_col] == 'A':
        print('Pizza is delivered on time! Next order...')
        field[new_row][new_col] = 'P'
        field[row][col] = '.'
        field[init_row][init_col] = 'B'
        row, col = new_row, new_col
        break
    elif field[new_row][new_col] == 'P':
        print('Pizza is collected. 10 minutes for delivery.')
        field[new_row][new_col] = 'R'
        field[row][col] = '.'
        row, col = new_row, new_col
        continue
    else:
        field[new_row][new_col] = 'B'
        if field[row][col] != 'R':
            field[row][col] = '.'
        row, col = new_row, new_col

for row in field:
    print(f'{"".join(row)}')
