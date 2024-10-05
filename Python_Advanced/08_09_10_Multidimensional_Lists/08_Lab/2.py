# rows = int(input())
# matrix = []
# for row in range(rows):
#     sublist = [int(x) for x in input().split(', ')]
#     even = []
#     for element in sublist:
#         if element % 2 == 0:
#             even.append(element)
#     matrix.append(even)
# print(matrix)

rows = int(input())
matrix = []
for row in range(rows):
    sublist = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(sublist)
print(matrix)
