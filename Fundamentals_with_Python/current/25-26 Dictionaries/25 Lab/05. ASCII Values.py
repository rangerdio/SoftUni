char_list, chars = input().split(", "), {}
[chars.update({letter: ord(letter)}) for letter in char_list]
