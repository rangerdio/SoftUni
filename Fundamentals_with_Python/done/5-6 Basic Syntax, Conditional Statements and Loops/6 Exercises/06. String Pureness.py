n = int(input())

for str_ in range(n):
    string = input()
    is_pure = True
    for index, letter in enumerate(string):
        if letter == "," or letter == "." or letter == "_":
            is_pure = False
    if is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
