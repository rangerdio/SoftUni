max_rows, max_cols = [int(x) for x in input().split(',')]
row, col = None, None
area = []
cheese = 0
danger = False

for r in range(max_rows):
    line = list(input())
    area.append(line)
    if 'M' in line:
        row = r
        col = line.index('M')
    if "C" in line:
        cheese += line.count('C')

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    command = input()
    if command == "danger":
        print('Mouse will come back later!')
        danger = True
        break
    new_row, new_col = row + directions[command][0], col + directions[command][1]

    if not (0 <= new_row < max_rows and 0 <= new_col < max_cols):
        print('No more cheese for tonight!')
        break
    elif area[new_row][new_col] == '*':
        area[new_row][new_col] = 'M'
        area[row][col] = '*'
        row, col = new_row, new_col
    elif area[new_row][new_col] == '@':
        continue
    elif area[new_row][new_col] == 'T':
        area[new_row][new_col] = 'M'
        area[row][col] = '*'
        row, col = new_row, new_col
        print('Mouse is trapped!')
        break
    elif area[new_row][new_col] == 'C':
        area[new_row][new_col] = 'M'
        area[row][col] = '*'
        row, col = new_row, new_col
        cheese -= 1
        if not cheese:
            print('Happy mouse! All the cheese is eaten, good night!')
            break

for line in area:
    print(''.join(line))
