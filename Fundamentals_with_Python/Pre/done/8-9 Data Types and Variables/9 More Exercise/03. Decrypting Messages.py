key = int(input())
n = int(input())
for num in range(n):
    letter = input()
    letter_num = ord(letter)
    new_letter_num = letter_num + key
    print(chr(new_letter_num), end="")
