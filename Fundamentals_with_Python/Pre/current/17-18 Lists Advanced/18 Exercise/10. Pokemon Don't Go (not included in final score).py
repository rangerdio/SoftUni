def merge_(words_, command):
    new_words_string = ""
    for index in range(len(words_)):
        if int(command[1]) <= index <= int(command[2]):
            new_words_string += words_[index]
        else:
            word_mod = " " + words_[index] + " "
            new_words_string += word_mod
            print(new_words_string)

    return new_words_string.split()


string = "Ivo Johny Tony Bony Mony"
words = string.split()
print(words)
current_cmd_list = ["merge", "0", "3"]
words = merge_(words, current_cmd_list)
print(words)
print(current_cmd_list)
