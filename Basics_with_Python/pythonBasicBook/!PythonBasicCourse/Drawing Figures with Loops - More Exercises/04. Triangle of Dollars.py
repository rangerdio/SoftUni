number = int(input())
for line in range(number + 1):
    for entry in range(line):
        print("$ ", end="") if entry < line - 1 else print("$")
