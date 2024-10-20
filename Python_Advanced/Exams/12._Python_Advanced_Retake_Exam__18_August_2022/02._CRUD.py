SIZE = 6
matrix = [[x for x in input().split()] for r in range(SIZE)]
first_position = input().split(', ')
row, col = int(first_position[0][1:]), int(first_position[1][:-1])

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    data = input().split(', ')
    if data[0] == "Stop":
        break
    new_row = row + directions[data[1]][0]
    new_col = col + directions[data[1]][1]

    if data[0] == "Create":
        if matrix[new_row][new_col] == '.':
            matrix[new_row][new_col] = data[2]

    elif data[0] == "Update":
        if matrix[new_row][new_col].isalpha() or matrix[new_row][new_col].isdigit():
            matrix[new_row][new_col] = data[2]

    elif data[0] == "Delete":
        if matrix[new_row][new_col].isalpha() or matrix[new_row][new_col].isdigit():
            matrix[new_row][new_col] = '.'

    elif data[0] == "Read":
        if matrix[new_row][new_col].isalpha() or matrix[new_row][new_col].isdigit():
            print(matrix[new_row][new_col])

    row, col = new_row, new_col

for line in matrix:
    print(' '.join(str(x) for x in line))
