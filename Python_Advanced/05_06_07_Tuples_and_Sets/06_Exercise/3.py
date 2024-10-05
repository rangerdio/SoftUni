n = int(input())
uniques = set()
for _ in range(n):
    row = input().split(" ")
    for word in row:
        uniques.add(word)
print(*uniques, sep='\n')
