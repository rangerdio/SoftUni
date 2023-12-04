n = int(input())
l = int(input())
ll = 97 + l
flag1 = False
flag2 = False

for first in range(1, n + 1):
    for second in range(1, n + 1):
        for third in range(97, ll):
            for forth in range(97, ll):
                for fifth in range(1, n + 1):
                    while True:
                        flag1 = False
                        flag2 = False
                        if fifth <= first:
                            flag1 = True
                            break
                        elif fifth <= second:
                            flag2 = True
                            break
                        else:
                            break
                    if flag1 or flag2:
                        continue
                    print(f"{first}{second}{chr(third)}{chr(forth)}{fifth}", end=" ")
