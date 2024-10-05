rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for rows in range(rows)]

max_sum = None
a_max, b_max, c_max, d_max = None, None, None, None

for row in range(rows - 1):
    for col in range(cols - 1):
        a = matrix[row][col]
        b = matrix[row][col + 1]
        c = matrix[row + 1][col]
        d = matrix[row + 1][col + 1]
        current_sum = a + b + c + d
#        print(f"{row}, {col} (,{a}, {b}, {c}, {d}) -> {current_sum}")
        if max_sum is None or current_sum > max_sum:
            max_sum = current_sum
            a_max, b_max, c_max, d_max = a, b, c, d

print(a_max, b_max)
print(c_max, d_max)
print(max_sum)
