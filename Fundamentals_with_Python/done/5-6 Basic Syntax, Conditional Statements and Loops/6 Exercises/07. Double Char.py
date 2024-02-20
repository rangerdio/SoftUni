
while True:
    string = input()
    if string == "End":
        break
    if string == "SoftUni":
        continue
    for index, letter in enumerate(string):
        for _ in range(2):
            print(letter, end="")
    print("")
