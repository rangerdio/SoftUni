import re
text = input()

pattern = f''
matches = re.finditer(pattern, text)

emojis = []
for emoji in matches:
    emojis.append(emoji.group(2))

cool_threshold = 0
coolness_data = {}
for emoji in emojis:
    emoji_coolness = 0
    for letter in emoji:
        if letter.isalpha():
            emoji_coolness += ord(letter)
    cool_threshold += emoji_coolness

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
for emoji in emojis:
    print(emoji)
