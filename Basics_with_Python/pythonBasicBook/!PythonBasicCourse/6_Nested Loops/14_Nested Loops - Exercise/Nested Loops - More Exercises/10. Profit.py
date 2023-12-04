ones = int(input())
twos = int(input())
fives = int(input())
magic = int(input())

one_ = 0
two_ = 0
five_ = 0
for one in range(ones + 1):
    one_ = 1 * one
    for two in range(twos + 1):
        two_ = 2 * two
        for five in range(fives + 1):
            five_ = 5 * five
            if magic == one_ + two_ + five_:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {magic} lv.")
