n = int(input())
matrix = [[x for x in list(input())] for row in range(n)]
symbol_ = input()

row_pos = 'empty'
col_pos = "empty"
for row in range(len(matrix)):
    if symbol_ in matrix[row]:
        row_pos = row
        col_pos = matrix[row].index(symbol_)
print(f'{symbol_} does not occur in the matrix') if row_pos == 'empty' else print(f'({row_pos}, {col_pos})')
