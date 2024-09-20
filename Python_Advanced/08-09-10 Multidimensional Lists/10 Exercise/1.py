ss = [[x for x in row.split(" ") if x != ""] for row in input().split("|")]
for i in range(len(ss) - 1, -1, -1):
    print(*ss[i], end=" ")
