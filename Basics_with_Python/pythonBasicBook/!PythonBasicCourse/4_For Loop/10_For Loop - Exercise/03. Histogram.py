n = int(input())
p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0
for number in range(1, n + 1):
    num = int(input())
    if num < 200:
        p1_count += 1
    elif 200 <= num <= 399:
        p2_count += 1
    elif 400 <= num <= 599:
        p3_count += 1
    elif 600 <= num <= 799:
        p4_count += 1
    else:
        p5_count += 1
print(f"{(p1_count /n * 100):.2f}%")
print(f"{(p2_count /n * 100):.2f}%")
print(f"{(p3_count /n * 100):.2f}%")
print(f"{(p4_count /n * 100):.2f}%")
print(f"{(p5_count /n * 100):.2f}%")
