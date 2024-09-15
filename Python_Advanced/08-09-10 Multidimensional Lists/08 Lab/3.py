rows = int(input())
matrix = []
for row in range(rows):
    sublist = [int(x) for x in input().split(', ')]
    matrix.append(sublist)

flattened = []
for sublist in matrix:
    for element in sublist:
        flattened.append(element)
print(flattened)

# flattened = [num for sublist in matrix for num in sublist]


rows = int(input())
matrix = []
for row in range(rows):
    sublist = [int(x) for x in input().split(', ')]
    matrix.extend(sublist)
print(flattened)
