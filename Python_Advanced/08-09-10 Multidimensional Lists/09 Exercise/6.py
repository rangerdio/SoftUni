rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for row in range(rows)]

valid_coordinates = None


def check_coordinates(command_: list, rows_: int, cols_: int):
    if len(command_) != 4:
        return False
    row1_, col1_, row2_, col2_ = map(int, command_)
    if not (0 <= row1_ < rows_ and 0 <= col1_ < cols_ and 0 <= row2_ < rows_ and 0 <= col2_ < cols_):
        return False
    return True


while True:
    command = input().split()
    # print(command)
    if command[0] == "END":
        break
    swap = command[0]
    command = command[1:]
    # print(command)
    valid_coordinates = check_coordinates(command, rows, cols)
    # print(valid_coordinates)

    if swap != 'swap' or len(command) != 4 or not valid_coordinates:
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = [int(x) for x in command]

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(' '.join(row))
