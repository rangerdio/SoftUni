c_count = False
o_count = False
n_count = False
current_word = ""
written_word = current_word

letter = input()

while letter != "End":
    letter_num = ord(letter)
    if 65 <= letter_num <= 90 or 97 <= letter_num <= 122:  # Validating that the letter is from the latin alphabet
        letter = chr(letter_num)
        if (c_count and o_count ) and letter == "n":
            letter = " "
            c_count = False
            o_count = False
            n_count = False
            current_word += letter
            written_word += current_word
            #  print(written_word)
            current_word = ""
            #  print(current_word)
            #  letter = input()

        elif (c_count and n_count) and letter == "o":
            letter = " "
            c_count = False
            o_count = False
            n_count = False
            current_word += letter
            written_word += current_word
            #  print(written_word)
            current_word = ""
            #  print(current_word)
            #  letter = input()

        elif (o_count and n_count) and letter == "c":
            letter = " "
            c_count = False
            o_count = False
            n_count = False
            current_word += letter
            written_word += current_word
            #  print(written_word)
            current_word = ""
            #  print(current_word)
            #  letter = input()

        elif letter == "c" and c_count:  # when "c" is second time, then write it into word
            current_word += letter
            #  print(current_word)
            #  letter = input()
        elif letter == "o" and o_count:  # when "o" is second time, then write it into word
            current_word += letter
            #  print(current_word)
            #  letter = input()
        elif letter == "n" and n_count:  # when "n" is second time, then write it into word
            current_word += letter
            #  print(current_word)
            #  letter = input()
        elif letter == "c" and c_count is False:  # when "c" is for first time, skipp it
            c_count = True
            #  print(current_word)
            #  letter = input()
        elif letter == "o" and o_count is False:  # when "o" is for first time, skipp it
            o_count = True
            #  print(current_word)
            #  letter = input()
        elif letter == "n" and n_count is False:  # when "o" is for first time, skipp it
            n_count = True
            #  print(current_word)
            #  letter = input()
        else:
            current_word += letter
            #  print(current_word)
            #  letter = input()
        letter = input()
    else:  # If entered letter is not from latin alphabet (line 11), continue to check next letter
        #  print(current_word)
        letter = input()
        continue
print(written_word)