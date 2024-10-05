size = int(input())
jet_position = []
armour = 300
sky = []
enemies = 4

for row in range(size):
    line = list(input())
    if 'J' in line:
        jet_position = [row, line.index('J')]
    sky.append(line)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while armour > 0 and enemies > 0:
    row, col = jet_position[0], jet_position[1]
    command = input()
    new_row = row + directions[command][0]
    new_col = col + directions[command][1]

    if sky[new_row][new_col] == '-':
        sky[row][col] = '-'
        sky[new_row][new_col] = 'J'
        jet_position = [new_row, new_col]
        continue
    elif sky[new_row][new_col] == 'E':
        enemies -= 1
        sky[row][col] = '-'
        sky[new_row][new_col] = 'J'
        jet_position = [new_row, new_col]
        if enemies == 0:
            print('Mission accomplished, you neutralized the aerial threat!')

        else:
            armour -= 100
            if armour == 0:
                print(f'Mission failed, your jetfighter was shot down! Last coordinates [{new_row}, {new_col}]!')

    elif sky[new_row][new_col] == 'R':
        armour = 300

        sky[row][col] = '-'
        sky[new_row][new_col] = 'J'
        jet_position = [new_row, new_col]

for row in sky:
    print(''.join(row))
