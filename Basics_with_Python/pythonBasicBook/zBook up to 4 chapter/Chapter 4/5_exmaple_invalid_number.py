num = float(input())
range = (num >= 100 and num <= 200) or num == 0


if not range:
    print("invalid")