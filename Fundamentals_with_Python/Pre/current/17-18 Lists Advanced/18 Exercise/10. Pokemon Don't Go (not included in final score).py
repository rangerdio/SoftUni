def merge_(words_, command):
    range_ = len(words_)
    if int(command[1]) >= len(words_):
        return words_
    elif int(command[2]) > len(words_) > int(command[1]):
        range_ = int(command[2])

    new_words_string = ""
    for index in range(range_):
        if int(command[1]) <= index <= int(command[2]):
            new_words_string += words_[index]
        else:
            word_mod = " " + words_[index] + " "
            new_words_string += word_mod
    return new_words_string.split()


string = "IvoJohnyTonyBony Mony"
words = string.split()
print(words)
current_cmd_list = ["merge", "3", "4"]
words = merge_(words, current_cmd_list)
print(words)
print(current_cmd_list)
