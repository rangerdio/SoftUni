text = input()
result = ""
strength = 0

for index in range(len(text)):
    if text[index] == ">":
        strength += int(text[index + 1])
        result += text[index]

    elif text[index] != ">" and strength > 0:
        strength -= 1

    else:
        result += text[index]

print(result)
