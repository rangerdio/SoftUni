first_end = int(input())
second_end = int(input())
third_end = int(input())
if second_end >= 7:
    second_end = 7

for first in range(1, first_end + 1):
    if first % 2 != 0:
        continue
    for second in range(2, second_end + 1):
        is_continue = False
        for i in range(2, second):
            if second % i == 0:
                is_continue = True
                break
        if is_continue:
            continue
        for third in range(1, third_end + 1):
            if third % 2 != 0:
                continue
            print(f"{first} {second} {third}")
