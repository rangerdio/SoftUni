N = int(input())
value = 0
weight = 0
time = 1
quality = 0

for ball_num in range(1, N + 1):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight / current_time) ** current_quality
    if current_value >= value:
        value = int(current_value)
        weight = current_weight
        time = current_time
        quality = current_quality
    else:
        current_value = 0

print(f"{weight} : {time} = {value} ({quality})")
