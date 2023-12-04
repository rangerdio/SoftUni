N = int(input())
P = int(input())
if N % P != 0:
    total = N // P + 1
else:
    total = N // P
print(total)
