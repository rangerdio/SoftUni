text = input()
new = ""
for index, letter in enumerate(text):
    if index != len(text) - 1:
        if letter != text[index + 1]:
            new += letter
    else:
        new += letter
print(new)
