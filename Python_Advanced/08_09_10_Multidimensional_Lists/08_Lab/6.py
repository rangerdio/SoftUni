n = int(input())
matrix = [[x for x in list(input())] for row in range(n)]

for _ in range(n):
    matrix.append(list(input()))
symbol_ = input()
is_found = False

print(matrix)
row_pos = 'empty'
col_pos = "empty"
for row in range(len(matrix)):
    print('ss', matrix[row])
    if symbol_ in matrix[row]:
        is_found = True
        row_pos = row
        col_pos = matrix[row].index(symbol_)
        break
print(f'{symbol_} does not occur in the matrix') if not is_found else print(f'({row_pos}, {col_pos})')
