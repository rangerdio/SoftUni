rows, cols = [int(x) for x in input().split(', ')]
matrix = []
for row in range(rows):
    sublist = [int(x) for x in input().split()]
    matrix.append(sublist)
print(matrix)


for col in range(cols):
    summ = 0
    for row in range(rows):
        summ += matrix[row][col]
    print(summ)
