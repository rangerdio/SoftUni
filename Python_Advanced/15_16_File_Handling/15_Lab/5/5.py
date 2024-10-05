import re
with open('input.txt', 'r') as text:
    content = text.read()
    print(content)

hits = {}
with open('words.txt', 'r') as words_file:
    words = words_file.read().split()
    for word in words:
        word = word.strip()
        pattern = fr'\b{word}\b'
        matches = re.findall(pattern, content, re.IGNORECASE)
        hits[word] = len(matches)
for word, hit in hits.items():
    print(f'{word} - {hit}')
