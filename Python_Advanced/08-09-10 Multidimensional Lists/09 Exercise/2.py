rows = int(input())
matrix = [[int(x) for x in input().split()] for row in range(rows)]

primary = 0
secondary = 0

for i in range(rows):
    primary += matrix[i][i]
    secondary += matrix[i][-i - 1]

print(abs(primary - secondary))
