from collections import deque

n = int(input())
matrix = [[int(x) for x in input().split()] for row in range(n)]
bombs = deque([x for x in input().split()])


def check_coordinates(command_: list, rows_: int, cols_: int):
    if len(command_) != 2:
        return False
    row1_, col1_ = map(int, command_)
    if not (0 <= row1_ < rows_ and 0 <= col1_ < cols_):
        return False
    return True


while bombs:
    current_bomb = [int(x) for x in bombs.popleft().split(',')]
    row_current_bomb = current_bomb[0]
    col_current_bomb = current_bomb[1]
    explode_value = matrix[row_current_bomb][col_current_bomb]

    if explode_value <= 0:
        continue

    for row_index in range(row_current_bomb - 1, row_current_bomb + 2):
        for col_index in range(col_current_bomb - 1, col_current_bomb + 2):
            valid_coordinates = check_coordinates([row_index, col_index], n, n)
            if valid_coordinates:
                if row_index == row_current_bomb and col_index == col_current_bomb:
                    matrix[row_index][col_index] = 0
                elif matrix[row_index][col_index] > 0:
                    matrix[row_index][col_index] -= explode_value

summ = 0
alive_cnt = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            alive_cnt += 1
            summ += matrix[row][col]

print('Alive cells:', alive_cnt)
print('Sum:', summ)
for row in range(n):
    print(*matrix[row])
