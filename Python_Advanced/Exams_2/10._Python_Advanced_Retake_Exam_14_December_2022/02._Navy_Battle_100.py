size = int(input())
field, row, col, cruisers, life = [], None, None, [0, 0, 0], [0, 0, 0]

for r in range(size):
    line = list(input())
    if 'S' in line:
        row, col = r, line.index('S')
    field.append(line)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    command = input()
    next_row = row + directions[command][0]
    next_col = col + directions[command][1]
    if field[next_row][next_col] == '-':
        field[row][col] = '-'
        field[next_row][next_col] = 'S'
        row, col = next_row, next_col
    elif field[next_row][next_col] == '*':
        life.pop()
        field[row][col] = '-'
        field[next_row][next_col] = 'S'
        row, col = next_row, next_col
        if not life:
            print(f'Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!')
            # may be marine disappear
            break
    elif field[next_row][next_col] == 'C':
        cruisers.pop()
        field[row][col] = '-'
        field[next_row][next_col] = 'S'
        row, col = next_row, next_col
        if not cruisers:
            print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
            break

for line in field:
    print(''.join(line))
