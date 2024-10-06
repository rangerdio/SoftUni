size = int(input())
sea = []
player_position = []
whirlpool = False
for row in range(size):
    line = list(input())
    if 'S' in line:
        player_position = [row, line.index('S')]
    sea.append(line)

# print(sea)
# print(player_position)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

caught = 0
while True:
    # print(player_position)
    command = input()
    if command == 'collect the nets':
        break
    row, col = player_position
    new_row = (row + directions[command][0]) % size
    new_col = (col + directions[command][1]) % size

    if sea[new_row][new_col].isdigit():
        caught += int(sea[new_row][new_col])

        sea[row][col] = '-'
        sea[new_row][new_col] = 'S'
        player_position = [new_row, new_col]

    elif sea[new_row][new_col] == 'W':
        caught = 0
        whirlpool = True
        sea[row][col] = '-'
        sea[new_row][new_col] = 'S'
        player_position = [new_row, new_col]
        break
    elif sea[new_row][new_col] == '-':
        sea[row][col] = '-'
        sea[new_row][new_col] = 'S'
        player_position = [new_row, new_col]

if whirlpool:
    print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught.'
          f' Last coordinates of the ship: [{player_position[0]},{player_position[1]}]')
elif caught >= 20:
    print(f'Success! You managed to reach the quota!')
elif caught < 20:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - caught} tons of fish more.")

if 0 < caught:
    print(f'Amount of fish caught: {caught} tons.')
if not whirlpool:
    for line in sea:
        print(''.join(line))
