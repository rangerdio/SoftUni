a1 = int(input())
a2 = int(input())
n = int(input())
nn = int(n / 2) - 1

for str1 in range(a1, (a2 - 1) + 1):
    for str2 in range(1, (n - 1) + 1):
        for str3 in range(1, nn + 1):
            # str1_str = str(str1)
            str4 = str1

            if str4 % 2 == 1 and (int(str2) + int(str3) + str4) % 2 == 1:
                print(f"{chr(str1)}-{str2}{str3}{str4}")
            else:
                continue
