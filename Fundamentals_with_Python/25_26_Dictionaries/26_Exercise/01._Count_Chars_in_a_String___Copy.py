dictionary = {}
text = input()
for letter in text:
    if letter == " ":
        continue
    elif letter not in dictionary:
        dictionary[letter] = 1
    else:
        dictionary[letter] += 1
for key in dictionary.keys():
    print(f'{key} -> {dictionary[key]}')
