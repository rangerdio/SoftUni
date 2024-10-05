from string import punctuation


with open('text.txt', 'r+') as file:
    for index, content in enumerate(file):
        a, p = 0, 0
        line = f'Line {index + 1} '
        for i, char in enumerate(content):
            if char in punctuation:
                p += 1
            elif char.isalpha():
                a += 1
            line += char
        line = line.rstrip()
        print(f'{line} ({a})({p})')
