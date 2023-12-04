# import sys
# n = int(input())
# min_number = sys.maxsize
# max_number = - sys.maxsize
#
# for number in range(1, n + 1):
#     asd = int(input())
#     if asd <= min_number:
#         min_number = asd
#     if asd >= max_number:
#         max_number = asd
# print(f"Max number: {max_number}")
# print(f"Min number: {min_number}")
n = int(input())
number = int(input())
min_number = number
max_number = number
for number in range(1, n):
    asd = int(input())
    if asd <= min_number:
        min_number = asd
    if asd >= max_number:
        max_number = asd
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
