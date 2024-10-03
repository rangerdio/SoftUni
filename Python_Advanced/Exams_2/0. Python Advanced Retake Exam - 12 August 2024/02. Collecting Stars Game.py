size = int(input())

stars = 2
player_position = []
field = []
for row in range(size):
    line = input().split()
    if 'P' in line:
        player_position = [row, line.index('P')]
    field.append(line)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    command = input()
    row, col = player_position[0], player_position[1]

    new_row = row + directions[command][0]
    new_col = col + directions[command][1]

    if 0 <= new_row < size and 0 <= new_col < size:
        # inside the field
        if field[new_row][new_col] == '*':
            stars += 1
            player_position = [new_row, new_col]
            field[new_row][new_col] = 'P'
            field[row][col] = '.'
            if stars == 10:
                break

        elif field[new_row][new_col] == '#':
            stars -= 1
            if stars == 0:
                break

        else:  # '.'
            player_position = [new_row, new_col]
            field[new_row][new_col] = 'P'
            field[row][col] = '.'

    else:
        # teleported to 0,0
        new_row, new_col = 0, 0
        if field[new_row][new_col] == "*":
            stars += 1
            player_position = [new_row, new_col]
            field[new_row][new_col] = 'P'
            field[row][col] = '.'
            if stars == 10:
                break

        else:
            player_position = [new_row, new_col]
            field[new_row][new_col] = 'P'
            field[row][col] = '.'

for row in field:
    print(' '.join(row))
