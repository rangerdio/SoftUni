ss = input().split("|")

matrix = []
for i in range(len(ss) - 1, -1, - 1):
    row = ss[i].split()
    if row:
        matrix.append(row)

for row in matrix:
    print(" ".join(row), end=" ")
