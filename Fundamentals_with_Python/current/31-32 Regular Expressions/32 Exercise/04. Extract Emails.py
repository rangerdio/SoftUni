import re
text = input()
pattern = r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
matches = re.findall(pattern, text)
for match in matches:
    print(match)
