start = int(input())
end = int(input())
for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):
        for num3 in range(start, end + 1):
            for num4 in range(start, end + 1):
                mark = False
                if num1 % 2 == 0 and num4 % 2 == 0:
                    continue
                elif num1 % 2 == 0 and num4 % 2 != 0:
                    mark = True
                if num1 % 2 != 0 and num4 % 2 != 0:
                    continue
                elif num1 % 2 != 0 and num4 % 2 == 0:
                    mark = True
                if mark and num1 > num4 and (num2 + num3) % 2 == 0:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")
