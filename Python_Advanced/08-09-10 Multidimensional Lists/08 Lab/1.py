rows, cols = [int(x) for x in input().split(', ')]
matrix = []
summ = 0

for row in range(rows):
    sublist = [int(x) for x in input().split(', ')]
    matrix.append(sublist)
    summ += sublist

print(summ)
print(matrix)
