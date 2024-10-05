import sys
n = input()
min_number = sys.maxsize
while n != "Stop":
    n = int(n)
    if n <= min_number:
        min_number = n
    n = input()
print(min_number)

# import sys
# n = input()
# min_number = sys.maxsize
# while True:
#     if n == "Stop":
#         break
#     n = int(n)
#     if n <= min_number:
#         min_number = n
#     n = input()
# print(min_number)
