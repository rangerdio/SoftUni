size = int(input())
matrix = [[int(x) for x in input().split()] for row in range(size)]
summ = 0
for i in range(size):
    summ += matrix[i][i]
print(summ)
