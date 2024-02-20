number = float(input())
magic = ""
part_1 = ""
part_adds = ""

if number == 0:
    part_1 = "zero"
elif number > 0:
    part_1 = "positive"
elif number < 0:
    part_1 = "negative"

if 0 != abs(number) < 1:
    part_adds = "small"
elif abs(number) > 1000000:
    part_adds = "large"
print(f"{part_adds} {part_1}")
