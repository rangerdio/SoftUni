synonyms = {}
n = int(input())

for i in range(n):
    word = input()
    synonym = input()
    synonyms.update({word: [synonym]}) if word not in synonyms.keys() else synonyms[word].append(synonym)

[print(f"{word} - {', '.join(synonym)}") for word, synonym in synonyms.items()]
