max_number = int(input())

for l in range(1, max_number + 1):
    print("")
    for c in range(l):
        print("*", end="")
for l in range(max_number - 1, 0, -1):
    print("")
    for c in range(l):
        print("*", end="")
#
# import time
# max_number = int(input())
#
# for l in range(1, max_number + 1):
#     time.sleep(0.08)
#     print("")
#     for c in range(l):
#         time.sleep(0.08)
#         print("*", end="")
# for l in range(max_number - 1, 0, -1):
#     time.sleep(0.08)
#     print("")
#     for c in range(l):
#         time.sleep(0.08)
#         print("*", end="")
