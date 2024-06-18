import re

text = input()

pattern_emo = r'(::|\*{2})([A-Z]{1}[a-z]{2,})\1'
matches = list(re.finditer(pattern_emo, text))

pattern_threshold = r'(\d)'
matches_threshold = (re.findall(pattern_threshold, text))
threshold = 1
for match in matches_threshold:
    threshold *= int(match)

emojis = []
for match in matches:
    emojis.append(f'{match.group(1)}{match.group(2)}{match.group(1)}')

cool_emos = []
for emoji in emojis:
    emoji_coolness = 0
    for letter in emoji:
        if letter.isalpha():
            emoji_coolness += ord(letter)
    if emoji_coolness >= threshold:
        cool_emos.append(emoji)

print(f'Cool threshold: {threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
for emo in cool_emos:
    print(emo)
