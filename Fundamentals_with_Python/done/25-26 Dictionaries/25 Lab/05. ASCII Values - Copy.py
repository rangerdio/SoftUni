characters = input().split(", ")
dictionary = {}
for character in characters:
    dictionary[character] = ord(character)
print(dictionary)
