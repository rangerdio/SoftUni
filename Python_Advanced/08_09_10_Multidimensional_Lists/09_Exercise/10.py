from collections import deque

n, m = [int(x) for x in input().split()]
matrix = [list(input()) for row in range(n)]
commands = deque(list(input()))
win_loose_coordinates = []


def check_positions(matrix_):
    player_start_positions_ = []
    bunny_start_positions_ = []
    for row in range(len(matrix_)):
        for col in range(len(matrix_[row])):
            if matrix_[row][col] == 'B':
                bunny_start_positions_.append([row, col])
            elif matrix_[row][col] == 'P':
                player_start_positions_ = [row, col]
    return player_start_positions_, bunny_start_positions_


def player_move(matrix_, player_start_positions_, current_command_):
    is_win_ = None
    win_loose_coordinates_ = []
    move = {
        'U': [player_start_positions_[0] - 1, player_start_positions_[1]],
        'D': [player_start_positions_[0] + 1, player_start_positions_[1]],
        'L': [player_start_positions_[0], player_start_positions_[1] - 1],
        'R': [player_start_positions_[0], player_start_positions_[1] + 1]
    }
    if (move[current_command_][0] < 0 or move[current_command_][0] >= n) or (
            move[current_command_][1] < 0 or move[current_command_][1] >= m):
        matrix_[player_start_positions_[0]][player_start_positions_[1]] = '.'
        win_loose_coordinates_ = [player_start_positions_[0], player_start_positions_[1]]
        is_win_ = True
        return matrix_, win_loose_coordinates_, is_win_, win_loose_coordinates_

    new_player_positions_ = move[current_command_]
    matrix_[player_start_positions_[0]][player_start_positions_[1]] = '.'
    destination = matrix_[new_player_positions_[0]][new_player_positions_[1]]

    if destination == '.':
        matrix_[new_player_positions_[0]][new_player_positions_[1]] = 'P'
    else:
        matrix_[new_player_positions_[0]][new_player_positions_[1]] = 'B'
        win_loose_coordinates_ = [new_player_positions_[0], new_player_positions_[1]]
        is_win_ = False

    return matrix_, new_player_positions_, is_win_, win_loose_coordinates_


counter = 0
is_win = None

while commands:
    if is_win is not None:
        break
    player_start_positions, bunny_start_positions = check_positions(matrix)
    if not player_start_positions:
        break
    current_command = commands.popleft()
    matrix, new_player_positions, is_win, win_loose_coordinates = player_move(matrix, player_start_positions, current_command)
    player_start_positions = new_player_positions

    # bunny move
    for current_bunny in bunny_start_positions:
        left_cell = [current_bunny[0], current_bunny[1] - 1]
        right_cell = [current_bunny[0], current_bunny[1] + 1]
        up_cell = [current_bunny[0] - 1, current_bunny[1]]
        down_cell = [current_bunny[0] + 1, current_bunny[1]]

        if 0 <= current_bunny[1] - 1:
            if matrix[current_bunny[0]][current_bunny[1] - 1] == 'P':
                matrix[current_bunny[0]][current_bunny[1] - 1] = 'B'
                win_loose_coordinates = [current_bunny[0], current_bunny[1] - 1]
                is_win = False
            elif matrix[current_bunny[0]][current_bunny[1] - 1] == '.':
                matrix[current_bunny[0]][current_bunny[1] - 1] = 'B'
        if current_bunny[1] + 1 < m:
            if matrix[current_bunny[0]][current_bunny[1] + 1] == 'P':
                matrix[current_bunny[0]][current_bunny[1] + 1] = 'B'
                win_loose_coordinates = [current_bunny[0], current_bunny[1] + 1]
                is_win = False
            elif matrix[current_bunny[0]][current_bunny[1] + 1] == '.':
                matrix[current_bunny[0]][current_bunny[1] + 1] = 'B'
        if 0 <= current_bunny[0] - 1:
            if matrix[current_bunny[0] - 1][current_bunny[1]] == 'P':
                matrix[current_bunny[0] - 1][current_bunny[1]] = 'B'
                win_loose_coordinates = [current_bunny[0] - 1, current_bunny[1]]
                is_win = False
            elif matrix[current_bunny[0] - 1][current_bunny[1]] == '.':
                matrix[current_bunny[0] - 1][current_bunny[1]] = 'B'
        if current_bunny[0] + 1 < n:
            if matrix[current_bunny[0] + 1][current_bunny[1]] == 'P':
                matrix[current_bunny[0] + 1][current_bunny[1]] = 'B'
                win_loose_coordinates = [current_bunny[0] + 1, current_bunny[1]]
                is_win = False
            elif matrix[current_bunny[0] + 1][current_bunny[1]] == '.':
                matrix[current_bunny[0] + 1][current_bunny[1]] = 'B'

    if is_win is not None:
        break

for row in range(n):
    print(''.join(matrix[row]))
print('won:', *win_loose_coordinates) if is_win else print('dead:', *win_loose_coordinates)
