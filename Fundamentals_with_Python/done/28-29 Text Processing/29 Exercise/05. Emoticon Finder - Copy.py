text = input()
emos = []
for index, letter in enumerate(text):
    if letter == ":":
        emos.append(letter + text[index + 1])
for emo in emos:
    print(emo)
