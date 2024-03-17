import re
names = input()
regex = r"\b[A-Z][a-z]* \b[A-Z][a-z]*\b"
result = re.findall(regex, names)
print(" ".join(result))
