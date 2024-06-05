import re
text = input()
pattern = r'(\||#)([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1((?:[0-9]\d{0,3}|10000))\1'
matches = list(re.finditer(pattern, text))

foods = {}
total_cal = 0
for match in matches:
    cal = int(match[4])
    total_cal += cal
print(f'You have food to last you for: {total_cal // 2000} days!')

# matches = re.finditer(pattern, text)
for match in matches:
    print(f'Item: {match.group(2)}, Best before: {match.group(3)}, Nutrition: {match.group(4)}')

