n = int(input())
even = 0
odd = 0
for number in range(1, n + 1):
    num = int(input())
    if number % 2 == 0:
        even += num
    else:
        odd += num
if even == odd:
    print(f"Yes")
    print(f"Sum = {even}")
else:
    print(f"No")
    print(f"Diff = {abs(even - odd)}")
