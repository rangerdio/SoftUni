word = input()
reversed_word = ""

for index in range(len(word) - 1, -1, -1):
    reversed_word += word[index]

print(reversed_word)

# print(word[::-1])
