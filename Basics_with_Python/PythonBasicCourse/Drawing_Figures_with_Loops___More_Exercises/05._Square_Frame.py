n = int(input())

for line in range(1, n + 1):
    for pos in range(1, n + 1):

        if line == 1 or line == n:
            if pos == 1:
                print("+ ", end="")
            elif pos == n:
                print("+")
            else:
                print("- ", end="")

        elif line != 1 and line != n:
            if pos == 1:
                print("| ", end="")
            elif pos == n:
                print("|")
            else:
                print("- ", end="")
