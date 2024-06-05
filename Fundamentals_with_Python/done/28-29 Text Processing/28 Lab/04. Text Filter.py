banned = input().split(", ")
text = input()
for word in banned:
    new_word = "*" * len(word)
    if word in text:
        text = text.replace(word, new_word)
print(text)
