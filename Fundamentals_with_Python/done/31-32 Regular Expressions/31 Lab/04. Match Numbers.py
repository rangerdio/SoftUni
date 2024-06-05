import re
line = input()
regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

result = re.finditer(regex, line)

for element in result:
    print(element.group(), end=" ")
