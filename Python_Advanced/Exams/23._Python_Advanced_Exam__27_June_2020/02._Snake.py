size = int(input())
field = []
row, col = None, None
food = 0

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


def find_next_burrow(field_, size_):
    for nr in range(size_):
        for nc in range(size_):
            if field_[nr][nc] == 'B':
                return nr, nc
    return None, None


while True:
    if food == 10:
        print('You won! You fed the snake.')
        break
    command = input()
    next_row = row + directions[command][0]
    next_col = col + directions[command][1]

    if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size:
        field[row][col] = '.'
        print('Game over!')
        break
    if field[next_row][next_col] == '*':
        food += 1
    if field[next_row][next_col] == 'B':
        field[next_row][next_col] = '.'
        next_row, next_col = find_next_burrow(field, size)

    field[row][col] = '.'
    field[next_row][next_col] = 'S'
    row, col = next_row, next_col

print(f'Food eaten: {food}')
for line in field:
    print(''.join(line))
