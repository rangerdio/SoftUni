import re

n = int(input())
for i in range(n):
    text = input()
    pattern = r'^([A-Z][a-z]+ [A-Z][a-z]+)#{1,}([A-Z][a-z]+(?:&[A-Z][a-z]+)*)\d{2}([A-Z][a-z]+(?: [A-Z][a-z]+)* (?:JSC|Ltd\.))$'
    valid_data = list(re.finditer(pattern, text))

    name = ""
    position = ""
    company = ""

    if valid_data:
        for match in valid_data:
            name = match.group(1)
            position = match.group(2)
            company = match.group(3)

        position = position.replace("&", " ")

        print(f'{name} is {position} at {company}')
