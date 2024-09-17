r, c = [int(x) for x in input().split()]

start_letter_row_num = 97
start_letter_cow_num = 96
matrix = []
for row in range(r):
    sublist = []
    start_letter_cow_num += 1

    for col in range(c):
        sublist.append(chr(start_letter_row_num + row) + chr(start_letter_cow_num + col) + chr(start_letter_row_num + row))
    matrix.append(sublist)

for row in range(len(matrix)):
    print(*matrix[row])
