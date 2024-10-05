

text = input()
vowels = ["a", "o", "u", "e", "i"]
new_text = ""
new_text = [new_text + letter for letter in text if letter.lower() not in vowels]
new_text = "".join(new_text)
print(new_text)


# new_text for letter in text if lower(letter) == "a"

# for letter in text:
#     if letter.lower() not in vowels:
#         new_text = new_text + letter
# print(new_text)


# print([num for num in range(11) if num % 2 == 0])



