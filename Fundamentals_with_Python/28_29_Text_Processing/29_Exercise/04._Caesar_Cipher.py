text = input()
encrypted = ""
for letter in text:
    encrypted += chr(ord(letter) + 3)
print(encrypted)
