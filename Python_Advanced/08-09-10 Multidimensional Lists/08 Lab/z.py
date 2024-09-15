# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# print(a[0][1])

a = []
for row in range(5):
    a.append([])
    for col in range(3):
        a[row].append(0)

print(a)

b = []
for row in range(5):
    sublist = []
    for col in range(3):
        sublist.append(0)
    b.append(sublist)
print(b)

c = []
for row in range(3):
    c.append([])
    for col in range(1, 4):
        c[row].append(col)
print(c)


d = []
for row in range(3):
    sublist = []
    for col in range(1, 4):
        sublist.append(col)
    d.append(sublist)
print(d)
