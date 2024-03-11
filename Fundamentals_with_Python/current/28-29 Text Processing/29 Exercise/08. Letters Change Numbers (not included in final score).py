def uppercase_front(word: str):
    letter = word[0].lower()
    letter_position = ord(letter) - 96
    number = ""
    for letter_ in word[1:]:
        if letter_.isnumeric():
            number += letter_
    number = int(number)
    return number / letter_position


def lowercase_front(word: str):
    letter = word[0].lower()
    letter_position = ord(letter) - 96
    number = ""
    for letter_ in word[1:]:
        if letter_.isdigit():
            number += letter_
    number = int(number)
    return number * letter_position


def uppercase_after(word: str, front_result_: float):
    letter = word[-1].lower()
    letter_position = ord(letter) - 96
    number = ""
    for letter_ in word[:-1]:
        if letter_.isdigit():
            number += letter_
    number = int(number)
    return front_result_ - letter_position


def lowercase_after(word: str, front_result_: float):
    letter = word[-1].lower()
    letter_position = ord(letter) - 96
    number = ""
    for letter_ in word[:-1]:
        if letter_.isdigit():
            number += letter_
    number = int(number)
    return front_result_ + letter_position


total = 0
line = input().split()

for current_word in line:
    front_result = 0
    after_result = 0
    if current_word[0].isupper():
        front_result = uppercase_front(current_word[:-1])
    elif current_word[0].islower():
        front_result = lowercase_front(current_word[:-1])

    if current_word[-1].isupper():
        after_result = uppercase_after(current_word[1:], front_result)

    elif current_word[-1].islower():
        after_result = lowercase_after(current_word[1:], front_result)
    total += after_result

print(f"{total:.2f}")
