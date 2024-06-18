def calculation(word: str):
    # print(f"for Word: {word}")
    word_total = 0
    lowered = word.lower()
    number = int(word[1:-1])

    if word[0].isupper():
        word_total = number / (ord(lowered[0]) - 96)
    elif word[0].islower():
        word_total = number * (ord(lowered[0]) - 96)

    if word[-1].isupper():
        word_total = word_total - (ord(lowered[-1]) - 96)
    elif word[-1].islower():
        word_total = word_total + (ord(lowered[-1]) - 96)

    return word_total


elements = input().split()
total = 0

for element in elements:
    total += calculation(element)

print(f"{total:.2f}")
