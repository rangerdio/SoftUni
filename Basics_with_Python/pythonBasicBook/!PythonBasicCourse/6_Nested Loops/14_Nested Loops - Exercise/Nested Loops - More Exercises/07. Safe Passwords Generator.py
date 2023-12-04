a = int(input())
b = int(input())
max_generated_pass = int(input())
counter = 0
flag1 = False
aa1 = 35
aa2 = 35
bb1 = 64
bb2 = 64
xx1 = 1
yy1 = 1
while counter <= max_generated_pass:
    if flag1:
        break
    for A1 in range(aa1, aa1 + 1):
        print(f"{chr(A1)}", end="")
        aa1 += 1
        if aa1 == 56:
            aa1 = 35

    for B1 in range(bb1, bb1 + 1):
        print(f"{chr(B1)}", end="")
        bb1 += 1
        if bb1 == 97:
            bb1 = 64

    for x in range(xx1, xx1 + 1):
        for y in range(yy1, yy1 + 1):
            print(f"{x}{y}", end="")
            if xx1 == a and yy1 == b:
                flag1 = True    # all combinations for "a" and "b"
            yy1 += 1
            if xx1 == a + 1 or yy1 == b + 1:
                yy1 = 1
                xx1 += 1
                break

    for B2 in range(bb2, bb2 + 1):
        print(f"{chr(B2)}", end="")
        bb2 += 1
        if bb2 == 97:
            bb2 = 64
    for A2 in range(aa2, aa2 + 1):
        print(f"{chr(A2)}", end="|")
        aa2 += 1
        if aa2 == 56:
            aa2 = 35
        counter += 1
        if counter == max_generated_pass:
            flag1 = True  # max combinations input parameter reached
