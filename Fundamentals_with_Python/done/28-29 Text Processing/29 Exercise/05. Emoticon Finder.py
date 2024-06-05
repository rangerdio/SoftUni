text = input()
emoticons = []
for index, letter in enumerate(text):
    if letter == ":" and index != -1:
        emoticons.append(letter + text[index + 1])
for emoticon in emoticons:
    print(emoticon, end="\n")
