# line = input()
line = "a3"
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

        if index + 1 > len(line):
            if line[index + 1].isdigit():
                continue
        else:  # number is gathered
            result_line += word.upper() * int(number_string)
            word = ""
            number_string = ""
for letter in result_line:
    unique[letter] = 1

print(f"Unique symbols used: {len(unique)}")
print(result_line)
