digits, letters, others = "", "", ""
line = input()
for letter in line:
    if letter.isdigit():
        digits += letter
    elif letter.isalpha():
        letters += letter
    else:
        others += letter
print(f"{digits}\n{letters}\n{others}")

