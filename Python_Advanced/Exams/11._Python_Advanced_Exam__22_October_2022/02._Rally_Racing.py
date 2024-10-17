size = int(input())
racing_number = input()
matrix = [[x for x in input().split(' ')] for r in range(size)]
mileage = 0
STEP = 10


def find_other_side(matr):
    for i in range(len(matr)):
        for j in range(len(matr)):
            if matr[i][j] == 'T':
                return i, j
    return None, None


directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

row, col = 0, 0
matrix[row][col] = 'C'

while True:
    command = input()
    if command == "End":
        print(f'Racing car {racing_number} DNF.')
        break
    new_row = row + directions[command][0]
    new_col = col + directions[command][1]

    if matrix[new_row][new_col] == 'F':
        print(f'Racing car {racing_number} finished the stage!')
        matrix[new_row][new_col] = 'C'
        matrix[row][col] = '.'
        mileage += STEP
        break

    if matrix[new_row][new_col] == 'T':
        matrix[new_row][new_col] = '.'
        new_row, new_col = find_other_side(matrix)
        mileage += STEP * 2

    mileage += STEP
    matrix[new_row][new_col] = 'C'
    matrix[row][col] = '.'
    row, col = new_row, new_col
    # print(matrix)
print(f'Distance covered {mileage} km.')
for line in matrix:
    print(''.join(line))
