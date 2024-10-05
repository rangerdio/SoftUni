hundreds_upper = int(input())
tents_upper = int(input())
units_upper = int(input())

for hundreds in range(2, hundreds_upper + 1):
    if hundreds % 2 != 0:
        continue
    for tents in range(1, tents_upper + 1):
        if 2 <= tents <= 7 and (tents == 7 or tents == 5 or tents == 3 or tents == 2):
            pass
        else:
            continue
        for units in range(2, units_upper + 1):
            if units % 2 != 0:
                continue
            else:
                print(hundreds, tents, units)
