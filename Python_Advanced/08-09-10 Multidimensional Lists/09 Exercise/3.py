rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for rows in range(rows)]

counter = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        a = matrix[row][col]
        b = matrix[row][col + 1]
        c = matrix[row + 1][col]
        d = matrix[row + 1][col + 1]
        if a == b and a == c and a == d:
            counter += 1
print(counter)
