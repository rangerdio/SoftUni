string_input = "text text text"
text_list = string_input.split()
# text_list = input().split()
letters = {}

for word in text_list:
    word = word.lower()

    for letter in word:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1


for letter, hits in letters.items():
    print(f"{letter} -> {hits}")
