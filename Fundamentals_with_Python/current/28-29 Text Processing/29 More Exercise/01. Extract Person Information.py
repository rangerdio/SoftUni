n = int(input())
lines = []
for i in range(n):
    lines.append(input())

for line in lines:
    if all(char in line for char in ("@", "|", "#", "*")):
        for index, letter in enumerate(line):
            if letter == "@":
                monkey_index = index
            elif letter == "|":
                pipe_index = index
            elif letter == "#":
                pound_index = index
            elif letter == "*":
                star_index = index
        if pipe_index - monkey_index > 1 and star_index - pound_index > 1:
            name = line[monkey_index + 1: pipe_index]
            age = line[pound_index + 1: star_index]
            print(f"{name} is {age} years old.")
