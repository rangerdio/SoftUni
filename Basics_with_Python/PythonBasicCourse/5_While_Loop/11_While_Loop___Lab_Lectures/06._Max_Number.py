import sys
n = input()
max_number = -sys.maxsize
while n != "Stop":
    n = int(n)
    if n >= max_number:
        max_number = n
    n = input()
print(max_number)

# import sys
# n = input()
# max_number = -sys.maxsize
# while True:
#     if n == "Stop":
#         break
#     n = int(n)
#     if n >= max_number:
#         max_number = n
#     n = input()
# print(max_number)
