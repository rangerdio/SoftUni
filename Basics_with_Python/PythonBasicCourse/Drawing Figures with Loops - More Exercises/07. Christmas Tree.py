n = 3

for i in range(0, n):
    for _ in range(n - i):
        print(" ", end="")
    for _ in range(n):
        print("*", end="")


    print("|")