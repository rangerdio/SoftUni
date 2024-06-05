line = input()
# line = "pesho>2sis>1a>2akarate>4hexmaster"
resulted_line = ""

strength = 0
# for index, letter in enumerate(line):
for index in range(len(line)):
    if line[index] == ">":
        strength += int(line[index + 1])
        resulted_line += line[index]
        continue

    if strength == 0:
        resulted_line += line[index]
    elif strength > 0:
        strength -= 1
print(resulted_line)

