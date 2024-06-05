line = input()
words = line.split()
for word in words:
    print(word * len(word), end="")
