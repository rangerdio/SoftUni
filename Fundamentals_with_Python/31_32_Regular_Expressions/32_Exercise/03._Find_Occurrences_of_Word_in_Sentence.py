import re
text = input()
word = input()
pattern = fr'\b{word}\b'
result = len(re.findall(pattern, text, re.I))
print(result)
