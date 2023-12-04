n = int(input())
maxDiff = 0
previous_pair = 0
current_pair = 0
for _num in range(1, n + 1):
    previous_pair = current_pair
    a = int(input())
    b = int(input())
    current_pair = a + b
    if previous_pair != current_pair and maxDiff < abs(previous_pair - current_pair) and _num != 1:
        maxDiff = abs(previous_pair - current_pair)
if maxDiff == 0:
    print(f"Yes, value={int(current_pair)}")
else:
    print(f"No, maxdiff={int(maxDiff)}")
