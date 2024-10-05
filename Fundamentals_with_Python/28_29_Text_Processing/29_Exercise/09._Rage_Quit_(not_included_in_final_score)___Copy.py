line = input()
unique = {}
result_line = ""

word = ""
number_string = ""
for index in range(len(line)):
    # print(line[index])
    if not line[index].isdigit():
        word += line[index]

    else:  # is digit
        number_string += line[index]

        if index + 1 >= len(line):
            result_line += word.upper() * int(number_string)
            word = ""
            number_string = ""
        else:  # number is gathered
            if line[index + 1].isdigit():
                continue
            result_line += word.upper() * int(number_string)
            word = ""
            number_string = ""

for letter in result_line:
    unique[letter] = 1


print(f"Unique symbols used: {len(unique)}")
print(result_line)
