number = int(input())
max_ = 0
boundary = int(input())
for current_num in range(1, boundary + 1):
    if current_num % number == 0:
        current_value = current_num
    else:
        continue
    if current_value > max_:
        max_ = current_value
print(max_)
