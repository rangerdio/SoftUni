char_list = input().split(", ")
chars = {}
[chars.update({letter: ord(letter)}) for letter in char_list]
print(chars)
