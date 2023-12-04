control = int(input())
hit_count = 0
never = True
flag1 = False
password = 0
for a in range(1, 10):
    for b in range(1, 10):
        if a < b:
            pass
        else:
            continue
        for c in range(1, 10):
            for d in range(1, 10):
                if c <= d:
                    continue
                else:
                    if a * b + c * d == control:
                        hit_count += 1
                        print(f"{a}{b}{c}{d}", end=" ")
                        if hit_count == 4:
                            never = False
                            password = str(a)+str(b)+str(c)+str(d)
if never:
    print()
    print("No!")
else:
    print()
    print(f"Password: {password}")
