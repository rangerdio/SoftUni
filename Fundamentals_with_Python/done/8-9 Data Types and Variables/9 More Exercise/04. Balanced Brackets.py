n = int(input())
balanced = True

open_mark = False
close_mark = False
for let in range(n):
    letter = input()
    if len(letter) > 1:
        continue

    if ord(letter) == 40:
        if open_mark is False:
            open_mark = True
            continue
        else:
            balanced = False
            break

    elif ord(letter) == 41:
        if open_mark is False:
            balanced = False
            break
        elif open_mark is True:
            open_mark = False  # reset
            close_mark = False  # reset
if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
