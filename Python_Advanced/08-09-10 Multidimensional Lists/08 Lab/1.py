rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for row in range(rows):
    sublist = [int(x) for x in input().split(', ')]
    matrix.append(sublist)

summ = 0
for row in range(len(matrix)):
    summ += sum(matrix[row])
print(summ)
print(matrix)
