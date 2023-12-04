from sys import maxsize
n = int(input())
max_num = - maxsize
ssum = 0
for number in range(1, n + 1):
    num = int(input())
    ssum += num
    if num > max_num:
        max_num = num
if ssum - max_num == max_num:
    print(f"Yes")
    print(f"Sum = {max_num}")
else:
    print(f"No")
    print(f"Diff = {abs(max_num - (ssum - max_num))}")
