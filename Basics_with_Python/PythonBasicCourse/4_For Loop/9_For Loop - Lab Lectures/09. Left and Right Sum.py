n = int(input())
total_left = 0
total_right = 0
for number in range(1,2 * n + 1):
    num = int(input())
    if number <= n:
        total_left += num
    if number > n:
        total_right += num
if total_right == total_left:
    print(f"Yes, sum = {total_right}")
else:
    print(f"No, diff = {abs(total_right-total_left)}")
