line = input()
words = []
numbers = []

current_str = ""
current_digit = ""
for letter in line:
    if letter.isdigit():
        current_digit += letter
        if current_str:
            words.append(current_str.upper())
            current_str = ""
    else:
        if current_digit:
            numbers.append(int(current_digit))
            current_digit = ""
        current_str += letter

if current_digit:
    numbers.append(int(current_digit))

if current_str:
    words.append(current_str)

uniq = "".join(words)

print(f"Unique symbols used: {len(set(uniq))}")

for index in range(len(words)):
    print(words[index] * numbers[index], end="")

