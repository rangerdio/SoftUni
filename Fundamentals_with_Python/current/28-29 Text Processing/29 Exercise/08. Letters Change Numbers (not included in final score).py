def uppercase_front(word: str):
    pass


def lowercase_front(word: str):
    pass


def uppercase_after(word: str):
    pass


def lowercase_after(word: str):
    pass

total = 0

line = "A12b s17G".split()
print(line)
for word_ in line:
    if word_[0].isupper():
        total += uppercase_front(word_)
    elif word_[0].islower():
        total += lowercase_front(word_)

    if word_[-1].isupper():
        total += uppercase_after(word_)
    elif word_[-1].islower():
        total += lowercase_after(word_)

print(f"{total:.2f}")
