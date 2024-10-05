import re


while True:
    line = input()
    if not line:
        break
    pattern = r"\d+"

    result = re.findall(pattern, line)
    for element in result:
        print(element, end=" ")
