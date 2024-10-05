import math
n = int(input())

if n == 1:
    print("*")
else:
    for line in range(1, n):
        if line != 1:
            print("")
        for _ in range(n - line):
            print(" ", end="")
        print("*", end="")
        for _ in range(line - 1):
            print(" *", end="")

    print("")
    for _ in range(1, n + 1):
        print("* ", end="")

    for line in range(1, n - 1):
        print("")
        for _ in range(line - 1):
            print(" ", end="")
        for _ in range(n - line):
            print(" *", end="")
    print("")
    for _ in range(1, n):
        print(" ", end="")
    if n != 1:
        print("*")
