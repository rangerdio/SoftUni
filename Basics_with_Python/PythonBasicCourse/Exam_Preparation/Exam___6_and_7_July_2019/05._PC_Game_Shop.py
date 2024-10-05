points1 =0
points2 = 0
for index, number1 in enumerate("Ivan"):
    num1 = (input())
    print(num1)
    if num1 == ord(number1):
        points1 += 10
    else:
        points1 += 2