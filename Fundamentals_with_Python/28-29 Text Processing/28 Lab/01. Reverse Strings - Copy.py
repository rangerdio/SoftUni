while True:
    line = input()
    if line == "end":
        break
    # result = "".join(reversed(line))
    result = line[::-1]
    print(f"{line} = {result}")
