# n = int(input())
# nums = ""
# counter = 1
# last_num = False
#
# for row in range(1, n + 1):
#     for cow in range(1, row + 1):
#         if counter > n:
#             last_num = True
#             break
#         #  print(str(counter) + " ", end="")
#         nums += (str(counter) + " ")
#         counter += 1
#     print(nums)
#     nums = ""
#     if last_num:
#         break
#     #  print()
#
counter = 0
n = int(input())
for r in range(1, n + 1):
    for c in range(1, r + 1):
        counter += 1
        if counter > n:
            break
        print(counter, end=" ")
    print()
