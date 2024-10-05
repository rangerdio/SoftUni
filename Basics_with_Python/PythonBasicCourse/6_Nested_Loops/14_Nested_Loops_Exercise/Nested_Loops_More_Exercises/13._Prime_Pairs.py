first_pair_start = int(input())
second_pair_start = int(input())
first_pair_diff = int(input())
second_pair_diff = int(input())
p1 = True
p2 = True
break_point = False
first_pair_end = first_pair_diff + first_pair_start
second_pair_end = second_pair_diff + second_pair_start
first_pair_str = ""
second_pair_str = ""
for first in range(first_pair_start, first_pair_end + 1):
    for second in range(second_pair_start, second_pair_end + 1):

        for n in range(2, second):
            p2 = True
            break_point = False
            if second % n == 0:
                p2 = False
                break_point = True
                break
        if break_point:
            continue

        for m in range(2, first):
            p1 = True
            break_point = False
            if first % m == 0:
                p1 = False
                break_point = True
                break
        if break_point:
            continue

        if p1 and p2:
            print(str(first)+str(second))
