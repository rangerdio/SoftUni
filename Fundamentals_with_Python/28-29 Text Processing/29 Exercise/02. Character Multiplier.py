def get_extension(words: list):  # get the additional value if one of the strings is longer than other
    adds_number = 0
    if len(words[0]) < len(words[1]):
        len_ = len(words[0])
        adds_string = words[1][len_::]
    else:
        len_ = len(words[1])
        adds_string = words[0][len_::]

    for letter in adds_string:
        adds_number += ord(letter)

    return adds_number


def get_calculation(strings_: list):    # calculate the value based on the shorter one
    total_number = 0
    string_1, string_2 = strings_[0], strings_[1]
    for i in range(len(string_1)):
        total_number += ord(string_1[i]) * ord(string_2[i])

    return total_number


strings = input().split()
if len(strings[0]) > len(strings[1]):   # make sure that first string is the shorter if different lenght
    strings[0], strings[1] = strings[1], strings[0]

print(get_calculation(strings) + get_extension(strings))
