size_rows, size_cols = [int(x) for x in input().split()]
playground = []
boy_row, boy_col = None, None

for row in range(size_rows):
    line = input().split()
    if 'B' in line:
        boy_row = row
        boy_col = line.index('B')
    playground.append(line)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}
touched = 0
moves = 0
while True:
    command = input()
    if command == 'Finish':
        break
    new_row = boy_row + directions[command][0]
    new_col = boy_col + directions[command][1]
    if not (0 <= new_row < size_rows and 0 <= new_col < size_cols) or playground[new_row][new_col] == 'O':
        continue
    if playground[new_row][new_col] == '-':
        playground[boy_row][boy_col] = '-'
        playground[new_row][new_col] = 'B'
        boy_row, boy_col = new_row, new_col
        moves += 1
    if playground[new_row][new_col] == 'P':
        playground[new_row][new_col] = 'B'
        playground[boy_row][boy_col] = '-'
        boy_row, boy_col = new_row, new_col
        touched += 1
        moves += 1
        if touched == 3:
            break

print(f'Game over!\nTouched opponents: {touched} Moves made: {moves}')
