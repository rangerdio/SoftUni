first_limit = int(input())
second_limit = int(input())
third_limit = int(input())
counter = 0
for first in range(1, first_limit + 1):
    if first % 2 != 0:
        continue
    for second in range(2, second_limit + 1):
        if second == 4 or second == 6 or second == 8 or second == 9:
            continue
        for third in range(1, third_limit + 1):
            if third % 2 != 0:
                continue
            print(f"{first} {second} {third}")
