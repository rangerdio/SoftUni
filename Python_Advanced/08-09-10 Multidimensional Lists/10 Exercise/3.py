rows = int(input())
cols = rows
matrix = [list(input()) for row in range(rows)]


def find_knights(matrix_: matrix):
    knights_ = []
    for row_ in range(len(matrix_)):
        for col_ in range(len(matrix_)):
            if matrix_[row_][col_] == 'K':
                knights_.append([row_, col_])
    return knights_


knights = find_knights(matrix)
moves = [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]
removed = 0

while True:
    max_hits = 0
    max_knight = [0, 0]

    for knight in knights:
        current_knight_row = knight[0]
        current_knight_col = knight[1]
        hits = 0
        
        for move in moves:
            dest_row = current_knight_row + move[0]
            dest_col = current_knight_col + move[1]
            if 0 <= dest_row < rows and 0 <= dest_col < cols and matrix[dest_row][dest_col] == 'K':
                hits += 1

        if hits > max_hits:
            max_hits = hits
            max_knight = [current_knight_row, current_knight_col]

    if max_hits == 0:
        break

    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = '0'
    removed += 1
print(removed)



