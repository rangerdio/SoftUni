ss = input().split("|")

matrix = []
for i in range(len(ss) -1, -1, -1):
    row = ss[i].split()
    if row:
        matrix.append(row)

for row in matrix:
    print(" ".join(row), end=" ")

# ss = [[x for x in row.split() if x] for row in input().split("|") if row]
# for i in range(len(ss) - 1, -1, -1):
#     print(" ".join(ss[i]), end=" ")
