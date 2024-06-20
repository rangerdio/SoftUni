math = input()
stack = []
for index, letter in enumerate(math):
    if letter == "(":
        stack.append(index)
    elif letter == ")":
        print(math[stack.pop():index + 1])
