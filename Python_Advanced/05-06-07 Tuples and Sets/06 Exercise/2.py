n, m = input().split(" ")
n = int(n)
m = int(m)

first = set()
second = set()

for i in range(n):
    first.add(input())
for i in range(m):
    second.add(input())

third = first.intersection(second)

print(*third, sep="\n")
