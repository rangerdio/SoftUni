text = input()
result = ""
for index, letter in enumerate(text):
    if index == len(text) - 1:
        result += letter
        break
    elif letter == text[index + 1]:
        pass
    else:
        result += letter
print(result)
