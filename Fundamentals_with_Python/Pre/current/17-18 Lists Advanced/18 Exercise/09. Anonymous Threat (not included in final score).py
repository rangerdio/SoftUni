def merge_(words_, command):
    range_upper = int(command[2])

    if int(command[1]) >= len(words_) - 1:
        return words_
    elif int(command[2]) >= len(words_) + 2 > int(command[1]):
        range_upper = len(words_)

    new_words_string = ""
    for index in range(len(words_)):
        if int(command[1]) <= index <= range_upper:
            new_words_string += words_[index]
        else:
            word_mod = " " + words_[index] + " "
            new_words_string += word_mod
    return new_words_string.split()


def divide_(words_, command):
    return "asd"


string = "abcd efgh ijkl mnop qrst uvwx yz"
words = string.split()
while True:
    current_cmd = input()
    current_cmd_list = current_cmd.split()
    if current_cmd == "3:1":
        break
    elif current_cmd_list[0] == "merge":
        words = merge_(words, current_cmd_list)
    elif current_cmd_list[0] == "divide":
        words = merge_(words, current_cmd_list)

print("".join(words))
