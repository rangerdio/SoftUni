rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for rows in range(rows)]

max_sum = None
max_row_1 = None
max_row_2 = None
max_row_3 = None

for row in range(rows - 2):
    current_sum = 0
    for col in range(cols - 2):
        a, b, c = matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]
        d, e, f = matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]
        g, h, i = matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]
        current_sum = sum((a, b, c, d, e, f, g, h, i))

        if max_sum is None or current_sum > max_sum:
            max_sum = current_sum
            max_row_1 = [a, b, c]
            max_row_2 = [d, e, f]
            max_row_3 = [g, h, i]

print('Sum =', max_sum)
print(*max_row_1)
print(*max_row_2)
print(*max_row_3)
