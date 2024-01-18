#text = input().split()
text = input()
print(text)
vowels = ["a", "o", "u", "e", "i"]
new_text = ""
#new_text for letter in text if lower(letter) == "a"

for letter in text:
    if letter.lower() not in vowels:
        new_text = new_text + letter
print(new_text)
